# Google ADK Agent Examples

A collection of progressive examples for building AI agents with [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/), covering the fundamentals from a basic agent through persistent storage and much more.

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- Google Gemini API key (or relevant provider keys per example)

## Setup

```bash
# Install dependencies
uv sync
# or
pip install -r requirements.txt
```

Create a `.env` file inside each example's agent folder with your API key:

```env
GOOGLE_API_KEY=your_key_here
```

## Dependencies

| Package | Purpose |
|---|---|
| `google-adk[database]` | Core ADK framework + SQLite session support |
| `google-generativeai` | Gemini model access |
| `litellm` | Multi-provider LLM support |
| `python-dotenv` | Environment variable management |
| `yfinance` | (Available for finance-related tool extensions) |
| `psutil` | (Available for system tool extensions) |
