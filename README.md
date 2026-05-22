# CV Analyser

A RAG pipeline that analyses CVs against job descriptions and produces structured, actionable feedback. Built to solve a specific problem: most students submitting applications have no visibility into why their CV fails at the ATS stage or what a recruiter actually sees.

## What it does

Upload a CV and paste a job description. The system scrapes and parses both, chunks the CV using linguistically-aware sentence segmentation, embeds the chunks, retrieves the most relevant sections against the job description, and passes the retrieved context to Gemini 2.5 Pro to generate a structured match analysis — match score, skills gap summary, and ranked improvement suggestions.

## Stack

Python, FastAPI, React, ChromaDB, Gemini 2.5 Pro API, spaCy, PyMuPDF, Pydantic

## Architecture

```
CV (PDF) ──> PyMuPDF parse ──> spaCy sentence segmentation ──> ChromaDB embeddings
                                                                        │
Job description ──> scraper ──> ChromaDB embeddings                    │
                                        │                               │
                                        └──── similarity retrieval ─────┘
                                                        │
                                                Gemini 2.5 Pro
                                                        │
                                              structured JSON output
                                          {match_score, skills_gap, suggestions}
```

**Why spaCy for chunking:** Early versions chunked by line or bullet point. This broke semantic coherence whenever a sentence spanned multiple lines or a CV used prose rather than bullets — retrieval was finding fragments that matched keywords but had lost surrounding context. spaCy's sentence segmentation uses a trained linguistic model to find sentence boundaries regardless of document formatting, producing chunks that are complete semantic units.

**Why ChromaDB:** Local vector store with no external service dependency. Appropriate for the scale of this project — per-request ephemeral collections rather than persistent storage.

**Why structured JSON output from Gemini:** The downstream consumer is a React frontend that needs to render discrete fields. Prose output requires brittle parsing. `response_mime_type="application/json"` enforces a consistent schema on every generation.

## Endpoints

```
POST /analyse     Upload CV + job description, returns structured match analysis
POST /chat        Follow-up questions about the analysis with conversation context
```

Both endpoints use Pydantic models for request validation. FastAPI returns 422 automatically on schema violations.


## Setup

```bash
# Clone and install
git clone https://github.com/A-Student4/CV-analyser.git
cd CV-analyser

# Backend
cd backend
pip install -r requirements.txt
python -m spacy download en_core_web_sm

# Copy env and add your Gemini API key
cp .env.example .env

# Run backend
uvicorn app.main:app --reload

# Frontend (separate terminal)
cd ../my-app
npm install
npm start
```

**Environment variables required:**
```
GEMINI_API_KEY=your_key_here
```

## Project structure

```
backend/
  app/
    routers/      API route handlers (/analyse, /chat)
    models/       Pydantic data models for CV parsing and response schemas
my-app/           React frontend
```
