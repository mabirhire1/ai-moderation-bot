# AI Moderation App (Hugging Face API)

This is a simple Python script that interacts with the OpenRouter Inference API to generate text from user input while applying basic moderation checks.
It rejects or redacts unsafe words like "kill", "hack", or "bomb" in both user input and AI output.

## Features

Accepts a user prompt from the command line.

Sends it to a OpenRouter model for text generation.

Blocks harmful input before sending to the API.

Redacts disallowed words in the AI response.

Gracefully handles API errors and invalid responses.

## Requirements

Python 3.8 or later

A Open Router account

A valid OpenRouter API Token

## Setup Instructions

Clone this repository

git clone https://github.com/your-username/ai-moderation-bot.git
cd ai-moderation-bot


Create and activate a virtual environment

python -m venv venv
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate         # For Windows


Install dependencies

pip install requests


## Run the App
python ai_moderation.py


You’ll be prompted to enter your question:

Enter your question (or 'quit' to exit): Where can I buy food?
AI: You can buy food at nearby grocery stores or restaurants.

If unsafe input is detected:

Enter your question (or 'quit' to exit): I want a bomb
Your input violated the moderation policy.
