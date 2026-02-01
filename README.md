# smart-translate-api

Smart Translate API is a FastAPI-based backend service that automatically detects the source language of input text and translates it into a target language using Google Cloud Translate.

The service is stateless, container-ready, and designed for cloud deployment.

---

## Features

- Automatic source language detection
- Translation using Google Cloud Translate
- Stateless REST API
- Docker-ready
- Cloud-deployable (Cloud Run / VM / Kubernetes)
- OpenAPI & Swagger documentation

---

## Tech Stack

- Python 3.10+
- FastAPI
- Google Cloud Translate v2
- Docker
- Uvicorn

---

## API Overview

### POST `/translate`

Translates input text into a target language.

#### Request Body

```json
{
  "text": "Hello world",
  "target": "fr"
}
