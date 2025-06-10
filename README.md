# Podcast IA em Português

Este projeto gera um podcast em áudio utilizando um modelo de linguagem e o F5‑TTS para síntese de voz em português do Brasil.

## Requisitos
- Python 3.12
- Dependências do `requirements.txt`
- Modelo F5‑TTS (configure `F5_MODEL_PATH` no arquivo `.env`)

## Uso rápido
1. Copie `.env.example` para `.env` e ajuste as variáveis.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal passando um prompt:
   ```bash
   python main.py "tema do podcast" --output output/podcast.mp3
   ```

O áudio final será salvo no caminho indicado.
