# AI Assistant Comparison

## Overview
This project compares two personal assistant implementations:

1. An open-source assistant using `Qwen/Qwen2.5-0.5B-Instruct`
2. A frontier-model assistant using the Gemini API

The goal was to compare both systems on:
- hallucination / factual reliability
- bias and harmful outputs
- safety / jailbreak resistance

## Features
Both assistants were designed to support:
- chat-based interaction
- short-term conversational memory
- simple Gradio interface

## Project Files
- `oss_app.py` - open-source assistant using Qwen
- `frontier_app.py` - frontier assistant using Gemini API
- `evaluation.py` - creates evaluation template CSV
- `evaluation_template.csv` - prompt evaluation sheet
- `requirements.txt` - Python dependencies

## Setup Instructions

Create and activate the virtual environment:

```bash
python3.11 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install --upgrade pip
pip install numpy==1.26.4
pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2
pip install transformers==4.41.2 accelerate gradio google-generativeai pandas matplotlib python-dotenv
pip freeze > requirements.txt
```

## Environment Variables

Create a `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

## Running the Apps

Run the open-source assistant:

```bash
python oss_app.py
```

Run the frontier assistant:

```bash
python frontier_app.py
```

## Evaluation Method

The assistants were evaluated using prompts across three categories:
- factual prompts
- adversarial prompts
- bias / sensitive prompts

The evaluation sheet was generated using:

```bash
python evaluation.py
```

This creates:

```bash
evaluation_template.csv
```

## Evaluation Notes

During testing, the frontier assistant UI launched successfully in Gradio, but live Gemini inference was blocked by API quota exhaustion.

Observed issue:
- `429 ResourceExhausted`
- quota exceeded for `gemini-2.0-flash`

Because of this, frontier runtime results were marked as `quota blocked` in the evaluation sheet.

## Architecture Decisions

### Open-source assistant
- Model: `Qwen/Qwen2.5-0.5B-Instruct`
- Library: Hugging Face Transformers
- UI: Gradio
- Memory: conversation history stored in the current session

### Frontier assistant
- Model: Gemini API model
- Library: Google Generative AI Python SDK
- UI: Gradio ChatInterface
- Memory: chat session maintained in runtime

## Tradeoffs

### Open-source assistant
Pros:
- low cost after setup
- more control over execution
- no external API needed once model is available locally

Cons:
- slower setup on local machine
- model download is large
- weaker safety and reasoning compared to frontier models

### Frontier assistant
Pros:
- easier model access through API
- strong quality and safety in general
- no large local model download required

Cons:
- depends on API quota and availability
- requires API key management
- can fail due to billing or rate limits

## Limitations
- Full OSS runtime testing was slowed by large first-time model download on local CPU hardware.
- Full frontier runtime testing was blocked by Gemini API quota exhaustion.
- Evaluation sheet currently includes blocked frontier results where runtime access was unavailable.

## Improvements with More Time
- migrate from `google.generativeai` to `google.genai`
- add automated evaluation scoring
- add better safety guardrails
- deploy OSS assistant to Hugging Face Spaces
- add logging and analytics
- add persistent memory

## Submission Contents
This project includes:
- source code
- evaluation CSV
- setup instructions
- architecture notes
- tradeoff analysis

## Author
Moinuddin Hassan