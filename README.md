# Podcast IA em Português

Projeto para gerar podcasts em português de forma leve. Utiliza a API Gemini para gerar o roteiro e oferece duas opções de síntese de voz: o modelo local F5‑TTS ou a solução leve baseada em `gTTS`.

## Requisitos
- Python 3.12
- Dependências do `requirements.txt`
- Chave da API Gemini (`GEMINI_API_KEY` no `.env`)
- (Opcional) Modelo F5‑TTS se desejar usar essa voz

## Uso rápido
1. Copie `.env.example` para `.env` e ajuste as variáveis.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal passando um prompt. Escolha a engine de voz (`simple` ou `f5`):
   ```bash
   python main.py "tema do podcast" --output output/podcast.mp3 --tts simple
   ```

O áudio final será salvo no caminho indicado.

## Testes e benchmark
Para rodar a suíte de testes e o benchmark básico:

```bash
python -m unittest
python benchmark.py
```
