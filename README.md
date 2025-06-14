# Podcast IA em Português

Este projeto converte documentos (PDF, DOCX ou TXT) em podcasts de forma leve utilizando apenas APIs gratuitas.

1. O texto é extraído do arquivo enviado.
2. Um resumo em português é gerado usando a API Gemini (Google AI Studio).
3. O resumo é convertido em áudio pelo Google Cloud Text-to-Speech (ou `gTTS` opcional).

## Requisitos
- Python 3.10+
- Variável `GEMINI_API_KEY` configurada no ambiente ou no `.env`.
- Para o Google TTS, configure `GOOGLE_APPLICATION_CREDENTIALS` apontando para o JSON da conta de serviço.
- Dependências do `requirements.txt`.

## Instalação
```bash
pip install -r requirements.txt
```

Copie `.env.example` para `.env` e adicione sua chave Gemini.

## Uso
```bash
python main.py arquivo.pdf --output resumo_podcast.mp3 --tts google
```
Você também pode usar `--tts simple` para gerar o áudio localmente com `gTTS`.

O resultado será salvo no caminho indicado.

### Síntese com ElevenLabs
Também é possível gerar áudio utilizando a API da ElevenLabs. Defina a variável
`ELEVEN_API_KEY` e execute o script `eleven_tts.py`:

```bash
export ELEVEN_API_KEY=sua_chave
python eleven_tts.py
```

O script lê `input.txt` e cria `output.mp3` com o modelo Flash v2.5.

## Testes
```bash
python -m unittest
```

## Benchmark
Um script `benchmark.py` mede tempo e memória de execução utilizando classes falsas.
```bash
python benchmark.py
```
