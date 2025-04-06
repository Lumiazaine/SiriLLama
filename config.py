# Parámetros
MEMORY_SIZE = 7  # Número de mensajes a recordar
ANSWER_SIZE_WORDS = 30  # Palabras por respuesta
MAX_TOKENS = ANSWER_SIZE_WORDS / 0.75  # Aproximación
CHUNCK_SIZE = 1024  # De vetorstore
CHUNK_OVERLAP = 200  # De vetorstore

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

PROVIDER = "ollama" 

OLLAMA_CHAT = "gemma3:latest"
OLLAMA_VISUAL_CHAT = "gemma3:latest"
OLLAMA_EMBEDDINGS_MODEL = "nextfire/paraphrase-multilingual-minilm:latest"
OLLAMA_BASE_URL = "http://host.docker.internal:11434"
