from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import gradio as gr
import pandas as pd
import re

df_clean=pd.read_csv('cleaned_data.csv')
# Load cleaned DataFrame with a link column
df = df_clean[['text', 'price_clean', 'location', 'facebookUrl']].copy()

# Clean numeric price column
df['price'] = pd.to_numeric(df['price_clean'], errors='coerce')

# Load MADAR-T5 (designed for Arabic dialects)
model_name = "UBC-NLP/AraT5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Simple Darija → MSA dictionary
darija_map = {
    "bghit": "أريد", "karhba": "سيارة", "auto": "سيارة", "voiture": "سيارة", "f": "في",
    "drahem": "مال", "kra": "إيجار", "souma": "سعر", "ta7t": "أقل من", "taht": "أقل من",
    "ghalya": "غالية", "rkhisa": "رخيصة", "wahran": "وهران", "oran": "وهران", "alger": "الجزائر",
    "dzayer": "الجزائر", "kayn": "يوجد", "chouf": "شاهد", "dir": "قم", "men": "من", "fi": "في",
    "3andi": "عندي", "nheb": "أريد", "tsoum": "تكلفة", "chwiya": "قليل", "bzaaf": "كثير",
    "mlih": "جيد", "marque": "ماركة", "modele": "موديل", "nif": "جديدة", "qdima": "قديمة"
}

def translate_darija_to_standard(text):
    words = text.lower().split()
    translated = [darija_map.get(word.strip(), word) for word in words]
    return " ".join(translated)

# Filter dataset based on simple rule-based logic
def search_cars(query):
    df_filtered = df.copy()

    # City filters
    if "وهران" in query:
        df_filtered = df_filtered[df_filtered['location'].str.contains("وهران", na=False)]
    if "الجزائر" in query:
        df_filtered = df_filtered[df_filtered['location'].str.contains("الجزائر", na=False)]

    # Price filtering
    match = re.search(r"أقل من (\d+)", query)
    if match:
        try:
            price_limit = int(match.group(1)) * 1000  # adjust as needed
            df_filtered = df_filtered[df_filtered['price'] < price_limit]
        except:
            pass

    return df_filtered.head(3).to_dict("records")

# Generate chatbot response
def generate_response(user_input):
    std_query = translate_darija_to_standard(user_input)

    # Optionally generate full prompt with MADAR-T5
    inputs = tokenizer.encode(std_query, return_tensors="pt", max_length=128, truncation=True)
    _ = model.generate(inputs)  # just to simulate transformer usage, for now not used in filtering

    results = search_cars(std_query)

    if len(results) > 0:
        response = f"🚗 Kayn {len(results)} 3roud li ykhdmouk:\n\n"
        for i, car in enumerate(results, 1):
            title = car['text']
            price = int(car['price'])
            city = car['location']
            link = car['facebookUrl']
            response += f"{i}. 🚙 {title}\n   💰 {price:,} \n   📍 {city}\n   🔗 [Voir annonce]({link})\n\n"
        response += "📩 T7eb nwarik kter?"
    else:
        response = "🫤 Ma l9it walou f had condition... Jرب بكلمات خرا wala souma okhra."

    return response

# Launch Gradio UI
gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="🚗 Chatbot Dziria - Car Market DZ",
    description="Sa9si 3la sayarat b darija, ou chatbot ywarik l3roud 📊",
    theme="default"
).launch()
