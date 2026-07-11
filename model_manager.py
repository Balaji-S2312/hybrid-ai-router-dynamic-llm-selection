from local_model import LocalModel
from fireworks_api import FireworksModel
from config import LOCAL_MODEL_NAME
from groq_api import GroqModel

class ModelManager:
    def __init__(self):
        self.local = LocalModel(LOCAL_MODEL_NAME)
        self.groq = GroqModel()

    def generate(self, model_name, prompt):
        if model_name == "local":
            return self.local.generate(prompt)

        elif model_name == "fireworks":   # temporary
            try:
                return self.groq.generate(prompt)
            except Exception as e:
                print(f"Cloud model unavailable: {e}")
                print("Falling back to local model...")
                return self.local.generate(prompt)

        else:
            raise ValueError(f"Unknown model: {model_name}")