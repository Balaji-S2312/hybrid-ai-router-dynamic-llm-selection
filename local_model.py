from transformers import pipeline


class LocalModel:

    def __init__(self, model_name):
        self.model_name = model_name

        self.generator = pipeline(
            task="text-generation",
            model=model_name
        )

    def generate(self, prompt, max_tokens=100):

        formatted_prompt = f"""<|system|>
You are a helpful AI assistant.

<|user|>
{prompt}

<|assistant|>
"""

        result = self.generator(
            formatted_prompt,
            max_new_tokens=max_tokens,
            do_sample=True,
            temperature=0.7,
            pad_token_id=self.generator.tokenizer.eos_token_id,
        )

        generated = result[0]["generated_text"]

        # Remove the prompt and return only the generated answer
        answer = generated[len(formatted_prompt):].strip()

        return answer

    def info(self):
        return {
            "model": self.model_name
        }