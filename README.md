# Sentiment Analysis API

A REST API that detects whether a piece of text is **positive**, **negative**, or **neutral** — built with FastAPI and a fine-tuned RoBERTa model trained on 124 million tweets.

## Demo

> Live demo: _coming soon_

![screenshot](https://placehold.co/800x400/0f172a/8bffe5?text=Sentiment+Analysis+API)

## Features

- Classifies text sentiment with a confidence score
- Understands modern slang, emoji, and informal language (Twitter-trained model)
- Interactive web UI — no setup needed for end users
- Auto-generated API docs at `/docs` (Swagger UI)
- JSON API for easy integration into any application

## Tech Stack

| Layer | Technology |
|---|---|
| API Framework | [FastAPI](https://fastapi.tiangolo.com/) |
| ML Model | [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) |
| ML Library | [Hugging Face Transformers](https://huggingface.co/docs/transformers) |
| Server | Uvicorn (ASGI) |
| Deployment | Railway |

## API Reference

### `POST /analyze`

Analyze the sentiment of a text string.

**Request body:**
```json
{
  "text": "This is absolutely amazing!"
}
```

**Response:**
```json
{
  "text": "This is absolutely amazing!",
  "sentiment": "positive",
  "confidence": 0.9821
}
```

| Field | Type | Description |
|---|---|---|
| `sentiment` | `string` | `positive`, `negative`, or `neutral` |
| `confidence` | `float` | Model confidence score (0–1) |

### `GET /health`

Returns `{"status": "ok"}` — useful for uptime monitoring.

## Run Locally

**Requirements:** Python 3.10+

```bash
# Clone the repo
git clone https://github.com/your-username/sentiment-api.git
cd sentiment-api

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

Open **http://localhost:8000** in your browser.

> The model (~500 MB) is downloaded automatically on first run.

## Project Structure

```
sentiment-api/
├── main.py           # FastAPI app + ML inference
├── static/
│   └── index.html    # Web UI
├── requirements.txt
├── Procfile          # Railway deployment config
└── README.md
```

## Known Limitations

- Input is capped at 512 tokens (model limit)
- Optimized for English text — other languages may be less accurate
- The model has no context memory — each request is analyzed independently

## Author

**Vasiliki Netsiou** — Full Stack Developer  
[LinkedIn](https://www.linkedin.com/in/vasiliki-netsiou) · [Portfolio](https://netsiou.dev)
