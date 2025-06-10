from transformers import pipeline


class LLM:
    def __init__(self, model_name: str = "pierreguillou/gpt2-small-portuguese", device: str = "cpu"):
        self.generator = pipeline("text-generation", model=model_name, device=0 if device == "cuda" else -1)

    def generate(self, prompt: str, max_new_tokens: int = 200) -> str:
        outputs = self.generator(prompt, max_new_tokens=max_new_tokens)
        return outputs[0]["generated_text"]
