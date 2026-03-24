import requests
from config import MODEL, OLLAMA_URL
import json
def ask_llm(prompt):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "temperature": 0.9,
            "top_p": 0.95,
            "repeat_penalty": 1.15
        }
    )

    text = ""

    for line in response.iter_lines():

        if line:
            data = json.loads(line.decode())
            text += data.get("response", "")

    return text