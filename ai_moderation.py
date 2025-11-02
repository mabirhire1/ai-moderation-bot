from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()

# Initialize the OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Banned keywords for moderation
BANNED_KEYWORDS = ["kill", "bomb", "hack", "terror", "attack"]

# Simple moderation function
def is_prompt_safe(prompt: str) -> bool:
    """Check if the input prompt violates moderation rules."""
    lowered = prompt.lower()
    for word in BANNED_KEYWORDS:
        if word in lowered:
            return False
    return True

def moderate_output(text: str) -> str:
    """Redact banned words in model output."""
    moderated = text
    for word in BANNED_KEYWORDS:
        moderated = moderated.replace(word, "[REDACTED]")
    return moderated

def main():
    print("\nAI Moderation & Response Generator (powered by OpenRouter)")
    print("Type 'quit' to exit.\n")

    while True:
        # Step 1: Accept user input
        user_input = input("Enter your question or message: ").strip()
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # Step 2: Input moderation
        if not is_prompt_safe(user_input):
            print("Your input violated the moderation policy.")
            continue

        # Step 3: System prompt to guide AI behavior
        system_prompt = (
            "You are a friendly and helpful AI assistant. "
            "Always respond politely, informatively, and avoid harmful or unsafe content."
        )

        try:
            # Step 4: Send to AI model via OpenRouter
            response = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://yourwebsite.com",  # Optional
                    "X-Title": "AI Moderation App",              # Optional
                },
                model="openai/gpt-4o-mini",  # lightweight and available on OpenRouter
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input},
                ]
            )

            ai_reply = response.choices[0].message.content

            # Step 5: Output moderation
            if not is_prompt_safe(ai_reply):
                print("The AI's response violated the moderation policy.")
            else:
                moderated_reply = moderate_output(ai_reply)
                print(f"\n AI Response:\n{moderated_reply}\n")

        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
