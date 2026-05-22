# AI Assistant Comparison

## Overview

This project compares two personal assistant implementations built with different model access strategies:

- **Open-source assistant** using `Qwen/Qwen2.5-0.5B-Instruct`
- **Frontier-model assistant** using the Gemini API

The goal was to compare both systems on:

- Hallucination / factual reliability
- Bias and harmful outputs
- Safety / jailbreak resistance

Both assistants were designed to support:

- Multi-turn chat-based interaction
- Short-term conversational memory
- Basic assistant-like behavior
- Lightweight Gradio interface

## Project Files

- `oss_app.py` - Open-source assistant using Qwen
- `frontier_app.py` - Frontier assistant using Gemini API
- `evaluation.py` - Generates the evaluation template CSV
- `evaluation_template.csv` - Prompt evaluation sheet
- `requirements.txt` - Python dependencies
- `report.pdf` - Final evaluation report
- `report.md` - Markdown version of the report

## Setup Instructions

### 1. Create and activate a virtual environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install numpy==1.26.4
pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2
pip install transformers==4.41.2 accelerate gradio google-generativeai pandas matplotlib python-dotenv
```

### 3. Add environment variables

Create a `.env` file and add:

```env
GEMINI_API_KEY=your_api_key_here
```

## Running the Apps

### Open-source assistant

```bash
python oss_app.py
```

### Frontier assistant

```bash
python frontier_app.py
```

## Evaluation Method

The assistants were evaluated using prompts across three categories:

- Factual prompts
- Adversarial / jailbreak prompts
- Bias / sensitive prompts

The evaluation sheet was generated with:

```bash
python evaluation.py
```

This creates:

- `evaluation_template.csv`

## Evaluation Notes

During testing, the frontier assistant UI launched successfully in Gradio, but live Gemini inference could not be completed because the API repeatedly returned quota exhaustion errors.

Observed issue:

- `429 ResourceExhausted`
- Quota exceeded for `gemini-2.0-flash`

Because of this, frontier runtime results were marked as **quota blocked** in the evaluation sheet instead of being treated as model-quality failures.

## Architecture Decisions

### Open-source assistant

- **Model:** `Qwen/Qwen2.5-0.5B-Instruct`
- **Library:** Hugging Face Transformers
- **UI:** Gradio
- **Memory:** Conversation history stored in the current session

### Frontier assistant

- **Model:** Gemini API model
- **Library:** Google Generative AI Python SDK
- **UI:** Gradio ChatInterface
- **Memory:** Chat session maintained in runtime

## Tradeoffs

### Open-source assistant

**Pros**
- Low cost after setup
- More control over execution
- No external API needed once the model is available locally

**Cons**
- Slower setup on local machine
- Large model download
- Weaker safety and reasoning compared to frontier models

### Frontier assistant

**Pros**
- Easy model access through API
- Strong quality and safety in general
- No large local model download required

**Cons**
- Depends on API quota and availability
- Requires API key management
- Can fail due to billing or rate limits

## Limitations

- Full OSS runtime testing was slower on local CPU hardware because of the large first-time model download.
- Full frontier runtime testing was blocked by Gemini API quota exhaustion.
- The evaluation sheet includes blocked frontier results where runtime access was unavailable.

## Improvements With More Time

- Migrate from `google.generativeai` to `google.genai`
- Add automated evaluation scoring
- Add stronger safety guardrails
- Add persistent memory
- Add better logging and analytics
- Expand the evaluation set with more systematic prompts

## Bonus Features

### Public OSS Deployment

The open-source assistant has been deployed publicly on Hugging Face Spaces using Gradio.

**Demo link:** https://huggingface.co/spaces/moinn07/ai-assistant-comparison

### Guardrails / Safety

A simple keyword-based safety layer blocks unsafe prompts such as bomb-making, hacking, and jailbreak-style requests before generation.

### Memory / Tool Use

The deployed OSS assistant supports short-term session memory across turns and includes a simple date/time tool.

### Observability

The deployed app logs interactions with timestamp, input, output, and latency into a CSV file for basic observability.

### Cost + Latency Table

| Platform | Hardware | Approx. Latency | Approx. Cost | Notes |
|---|---|---:|---:|---|
| Hugging Face Spaces | CPU Basic | 5–10s | $0 | Free public deployment |
| Hugging Face Spaces | Upgraded GPU | 1–3s | Paid | Better latency |
| RunPod | Small GPU | 1–2s | Pay-as-you-go | Better production option |
| Replicate | Hosted inference | 2–5s | Pay-per-use | Easy hosted deployment |

## Submission Contents

This project includes:

- Source code
- Evaluation CSV
- Setup instructions
- Architecture notes
- Tradeoff analysis
- Evaluation report PDF
- Public OSS demo link

## Author

**Moinuddin Hassan**
