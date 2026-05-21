from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Sentiment Analysis API")

# Load model once at startup — twitter-roberta understands modern slang/emoji
sentiment_model = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

# This model returns LABEL_0/1/2 — map to human-readable labels
LABEL_MAP = {"LABEL_0": "negative", "LABEL_1": "neutral", "LABEL_2": "positive"}


class TextInput(BaseModel):
    text: str


@app.get("/")
def index():
    return FileResponse("static/index.html")


@app.post("/analyze")
def analyze(input: TextInput):
    if not input.text.strip():
        return {"error": "Text cannot be empty"}

    result = sentiment_model(input.text[:512])[0]

    return {
        "text": input.text,
        "sentiment": LABEL_MAP.get(result["label"], result["label"].lower()),
        "confidence": round(result["score"], 4),
    }


@app.get("/health")
def health():
    return {"status": "ok"}


app.mount("/static", StaticFiles(directory="static"), name="static")
