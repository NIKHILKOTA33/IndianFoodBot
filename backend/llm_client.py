import requests


class LocalLLMClient:
    def __init__(self, model_name="tinyllama"):
        self.model_name = model_name
        self.api_url = "http://localhost:11434/api/generate"

    def generate_response(self, prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.api_url, json=payload)

        if response.status_code != 200:
            raise Exception(f"Ollama Error: {response.text}")

        return response.json().get("response", "")
