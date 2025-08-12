# This class is used for generate raw data from gpt-oss
# First you need to install ollama and gpt-oss to your computer
# Run it and check the status on http://localhost:11434
# If it works then you can send request to it


import requests

MODEL_NAME = "gpt-oss"

def get_flashcards():
    """Fetch flashcard text from local GPT-OSS via Ollama."""
    prompt = """
    Generate 5 vocabulary flashcards.
    Format each card as:
    Word: <word>
    Definition: <definition>
    Example: <example sentence>
    ---
    """

    res = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    data = res.json()
    return data["response"]

# Run the test to see if you can get data from gpt-oss
if __name__ == "__main__":
    print(get_flashcards())
