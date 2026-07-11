from openai import OpenAI
from config import FIREWORKS_API_KEY, FIREWORKS_MODEL

client = OpenAI(
    api_key=FIREWORKS_API_KEY,
    base_url="https://api.fireworks.ai/inference/v1",
)

class FireworksModel:

    def __init__(self):
        self.client = client

    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model=FIREWORKS_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content