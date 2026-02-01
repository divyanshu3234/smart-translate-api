from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.cloud import translate_v2 as translate
from fastapi.middleware.cors import CORSMiddleware
import html

app = FastAPI(
    title="Smart Translate API",
    description="Detects source language and translates text using Google Cloud Translate API.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production or set to ["http://localhost:3000"] for your frontend
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranslateRequest(BaseModel):
    text: constr(max_length=5000)
    target: str

def smart_translate_text(text: str, target_language: str) -> dict:
    client = translate.Client()

    detection = client.detect_language(text)
    source_language = detection["language"]

    if source_language == target_language:
        return {
            "source_language": source_language,
            "target_language": target_language,
            "translated_text": text,
            "note": "No translation needed"
        }

    translation = client.translate(
        text,
        target_language=target_language
    )

    return {
        "source_language": source_language,
        "target_language": target_language,
        "translated_text": html.unescape(
            translation["translatedText"]
        )
    }

@app.post("/translate")
def translate_endpoint(req: TranslateRequest):
    try:
        return smart_translate_text(req.text, req.target)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Translation failed"
        )
@app.get("/health")
def health():
    return {"status": "ok"}
