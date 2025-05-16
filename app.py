from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from langchain_groq import ChatGroq  
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

app = FastAPI()

# Get the absolute path to the templates directory
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

model = ChatGroq(model_name="gemma2-9b-it", groq_api_key=GROQ_API_KEY)
prompt = ChatPromptTemplate.from_template("Translate the following text to {language}: {text}")
chain = prompt | model | StrOutputParser()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate", response_class=HTMLResponse)
async def translate_text(request: Request, language: str = Form(...), text: str = Form(...)):
    try:
        translation = await chain.ainvoke({"language": language, "text": text})
        return templates.TemplateResponse(
            "translation_result.html",
            {
                "request": request,
                "original_text": text,
                "language": language,
                "translation": translation
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error_message": str(e)
            }
        )

if __name__ == "__main__":
    import uvicorn
    port = 8000
    uvicorn.run(app, host="127.0.0.1", port=port)