# 🚗 Algerian Cars Market Chatbot

An LLM-powered chatbot that helps users explore and analyze car listings from the Algerian used-car market. This intelligent assistant is hosted on **Hugging Face Spaces** and uses real car listing data scraped from **Facebook Marketplace**. What sets this project apart is its **deep understanding of Algerian dialects** using **DeepSeek V3 API**, enabling robust feature extraction from unstructured and noisy descriptions.

🌐 **Live Demo**: [dz_cars_market_chatbot on Hugging Face](https://huggingface.co/spaces/mgrine/dz_cars_market_chatbot)

---

## 🧠 Project Overview

This chatbot assists users in navigating the Algerian second-hand car market with natural language queries. It integrates:

- 💬 **Chat interface** for interactive queries
- 🔍 **Feature extraction from car descriptions using LLMs**
- 🇩🇿 **Algerian dialect support** with DeepSeek V3
- 🧾 Data scraped from **Facebook Marketplace Algeria** using **Apify**
- 🎛️ Deployed using **Streamlit** and hosted on **Hugging Face Spaces**

---

## 💡 Key Innovation: Feature Extraction with LLMs

The **core innovation** of this project is the use of **DeepSeek V3**, a large language model capable of **understanding and parsing Algerian dialect and informal Facebook language**, to extract structured car data from free-text descriptions.

🔍 **Extracted Features** from raw Facebook listings:
- 🏷️ **Brand & Model** (e.g., "Clio 4", "Peugeot 207")
- 📅 **Year of Manufacture**
- ⛽ **Fuel Type** (essence, diesel, etc.)
- 🔁 **Transmission** (manual, automatic)
- 📏 **Mileage (km)**
- ⚙️ **Condition** (new, used, to repair)
- 💰 **Asking Price**
- 📍 **Location hints**

➡️ These fields are not scraped directly but **extracted from messy, user-generated texts**, often written in **dialectal Arabic, French slang, or code-switching**. DeepSeek’s multilingual and instruction-following capabilities allow accurate and flexible extraction even when data is noisy or abbreviated.

✳️ **Few-shot prompts** are used to instruct DeepSeek on how to parse these fields, adapting to local linguistic variations (e.g., "ess", "mazout", "3aytli", "automatic", "dzair").

---

## 📦 Data Collection

- **Platform**: Facebook Marketplace Algeria
- **Scraping Tool**: [Apify Facebook Marketplace Scraper](https://apify.com/facebook/facebook-marketplace-scraper)
- **Fields scraped**: Post title, description, timestamp, image (if available)
- **Language Challenges**: Informal Arabic-French dialects, emojis, non-standard spelling

---

## 🗨️ Chatbot Usage Instructions

1. Visit the [Hugging Face Space](https://huggingface.co/spaces/mgrine/dz_cars_market_chatbot)
2. Ask in natural language, e.g.:
   - “عندك بيجو 207؟”
   - “I want a diesel Clio 4 under 200 million”
   - “Show me cars in Oran with automatic transmission”
3. The bot processes your request, uses LLM-based filtering, and returns matching listings

---

## 🧰 Technologies Used

| Component | Description |
|----------|-------------|
| 🐍 Python | Core programming language |
| 🧾 Apify | Used for scraping raw Facebook listings |
| 🤖 DeepSeek V3 | LLM API for multilingual & dialect-aware feature extraction |
| 🎛️ Streamlit | Interface for chatbot frontend |
| 🧠 Hugging Face Spaces | Hosting platform for app deployment |

---

## 🎯 Use Cases

- 🧠 NLP experimentation on dialectal Algerian text
- 🚙 Smart car recommendation based on structured info
- 📊 Market monitoring for brands, models, and prices
- 🛠️ Used car pricing and condition analysis

---

## ⚠️ Limitations

- Facebook Marketplace content structure may change
- Some descriptions are incomplete or ambiguous
- LLMs may require occasional prompt tuning for optimal results

---

## 👨‍💻 Author

**Grine Mohamel El Amine**  
Data Scientist | NLP Researcher – ESE Oran  
📧 [mgrine66@gmail.com](mailto:mgrine66@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/mohamed-grine-1267b32aa/)  
🧠 [Hugging Face](https://huggingface.co/mgrine)

---

## 📚 References

- DeepSeek V3 API: [https://platform.deepseek.com/](https://platform.deepseek.com/)
- Apify Scraper: [https://apify.com/facebook/facebook-marketplace-scraper](https://apify.com/facebook/facebook-marketplace-scraper)
- Hugging Face Spaces: [https://huggingface.co/spaces](https://huggingface.co/spaces)

---

## 📄 License

This project is available for **non-commercial, educational, and research purposes** under the MIT License.

