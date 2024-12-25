# Parameters
MEMORY_SIZE = 5  # Number of messages to remember
ANSWER_SIZE_WORDS = 30  # Number of words in an answer
MAX_TOKENS = ANSWER_SIZE_WORDS / 0.75  # rough approximation
CHUNCK_SIZE = 1024  # of vetorstore
CHUNK_OVERLAP = 200  # of vetorstore

# Prompts
PROMPT_CHAT = f"""Eres Siri LLama, una inteligencia artificial que responde SIEMPRE en español.
No uses inglés ni otro idioma a menos que sea estrictamente necesario.
La respuesta tiene aproximadamente {ANSWER_SIZE_WORDS} palabras y es informativa.
Si no entiendes la pregunta, pide más información.
"""
PROMPT_VISUAL_CHAT = """Eres Siri LLama, una inteligencia artificial que responde SIEMPRE en español.
No uses inglés ni otro idioma a menos que sea estrictamente necesario.
Has visto una imagen y describes su contenido en castellano.
"""

PROVIDER = "ollama"  # or "fireworks"
# Models
# Ollama

OLLAMA_CHAT = "gemma2:latest"
OLLAMA_VISUAL_CHAT = "llava:latest"
OLLAMA_EMBEDDINGS_MODEL = "0ssamaak0/nomic-embed-text:latest"
OLLAMA_BASE_URL = "http://host.docker.internal:11434"

# Fireworks
FIREWORKS_CHAT = "accounts/fireworks/models/llama-v3p1-8b-instruct"
FIREWORKS_VISUAL_CHAT = "accounts/fireworks/models/phi-3-vision-128k-instruct"
FIREWORKS_API_KEY = "<API_KEY>"
FIREWORKS_EMBEDDINGS_MODEL = "nomic-ai/nomic-embed-text-v1.5"
