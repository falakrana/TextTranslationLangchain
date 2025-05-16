# 🌍 AI-Powered Text Translation with LangChain & Groq

A high-performance translation API leveraging **Gemma 2B** via Groq's LPUs for sub-second translations, managed with LangChain and served via FastAPI.

## 🚀 Key Features
- **Lightning-fast translations** (<1s latency) using Groq's inference API
- **LangChain pipeline** for prompt templating and model management
- **Multi-language support** with state-of-the-art LLM translation
- **Production-ready API** built with FastAPI (async support)
- **Simple integration** via clean REST endpoints

## ⚙️ Tech Stack
- **Backend**: FastAPI (Python)
- **AI Pipeline**: LangChain
- **LLM**: Gemma 2B (via Groq)
- **Hardware Acceleration**: Groq LPUs

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/falakrana/TextTranslationLangchain.git
   cd TextTranslationLangchain

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Add your API key in .env file.

## Running app
1. Run with:
   ```bash
   python app.py

  API will be available at http://127.0.0.1:8000
  
  Interactive docs available at:
  - http://localhost:8000/docs (Swagger)
  - http://localhost:8000/redoc (ReDoc)
