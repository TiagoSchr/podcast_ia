"""Wrapper simples para consumo da API Gemini."""

import httpx

from .config import GEMINI_API_KEY


class LLM:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or GEMINI_API_KEY
        self.url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY não configurada")

    def generate(self, prompt: str, max_tokens: int = 200) -> str:
        """Envia o prompt para a API Gemini e retorna o texto gerado."""
        headers = {"X-Goog-Api-Key": self.api_key}
        data = {"contents": [{"parts": [{"text": prompt}]}], "generationConfig": {"maxOutputTokens": max_tokens}}
        response = httpx.post(self.url, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
