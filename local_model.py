import os
from huggingface_hub import InferenceClient

class LocalModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.client = InferenceClient(
            api_key=os.getenv("HF_TOKEN")
        )

    def generate(self, prompt, max_tokens=100):
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
        )

        return completion.choices[0].message.content

    def info(self):
        return {
            "model": self.model_name
        }