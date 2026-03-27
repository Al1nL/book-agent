import time
import requests
from config import MODEL, OLLAMA_URL
import json

MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds between retries


def ask_llm(prompt):

    last_error = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL,
                    "prompt": prompt,
                    "stream": True,
                    "options": {
                        "temperature": 0.9,
                        "top_p": 0.95,
                        "repeat_penalty": 1.15
                    }
                },
                timeout=300
            )
            response.raise_for_status()

            text = ""
            for line in response.iter_lines():
                if line:
                    data = json.loads(line.decode())
                    if "error" in data:
                        raise RuntimeError(f"Ollama error: {data['error']}")
                    text += data.get("response", "")

            if not text.strip():
                raise RuntimeError(
                    f"Ollama returned empty response for model '{MODEL}'. "
                    f"Is the model downloaded? Run: ollama pull {MODEL}"
                )

            return text

        except (requests.ConnectionError, requests.Timeout) as e:
            last_error = e
            if attempt < MAX_RETRIES:
                print(f"LLM call failed (attempt {attempt}/{MAX_RETRIES}): {e}. Retrying in {RETRY_DELAY}s...")
                time.sleep(RETRY_DELAY)
            else:
                raise RuntimeError(
                    f"Ollama unreachable after {MAX_RETRIES} attempts. "
                    f"Is Ollama running? Try: ollama serve\nLast error: {e}"
                ) from last_error

        except requests.HTTPError as e:
            raise RuntimeError(f"Ollama HTTP error: {e}") from e
