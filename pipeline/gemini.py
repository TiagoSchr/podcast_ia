"""Wrapper para resumir texto usando a API Gemini."""

from __future__ import annotations

import google.generativeai as genai

from .config import GEMINI_API_KEY


class Gemini:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or GEMINI_API_KEY
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY não configurada")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def summarize(self, text: str) -> str:
        prompt = (
            "Resuma o texto a seguir em português de forma didática utilizando aproximadamente 15% do tamanho original:\n"
            + text
        )
        response = self.model.generate_content(prompt)
        return response.text
