<div align = "center">
<h1>
    <img src = "https://github.com/0ssamaak0/SiriLLama/blob/main/assets/icon.png?raw=true" width = 200 height = 200>
<br>

</h1>

<h3>
Siri LLama
</h3>
</div>

Siri LLama es un atajo (shortcut) de Apple que permite acceder a modelos LLMs que se ejecutan localmente, ya sea a través de Siri o de la interfaz del atajo, en cualquier dispositivo Apple conectado a la misma red del servidor. Utiliza Langchain 🦜🔗 y es compatible con modelos de código abierto tanto de [Ollama](https://ollama.com/) 🦙 u otros.

# Descarga el [Shortcut](https://www.icloud.com/shortcuts/fd032a4e75cc4d81a6f9a742053d4c18)

# Comienzo
## Requisitos

1. Descargar [Git](https://git-scm.com/downloads/), puedes descargar el ejecutable o hacerlo por la terminal.


```bash
winget install --id=Git.Git  -e
```

2. Una vez descargado Git, descargamos el repositorio y nos dirigimos a él.

```bash
git clone https://github.com/Lumiazaine/SiriLLama.git #Descarga el repositorio de github
cd SiriLLama #Nos dirigimos a la ruta
```

### Instalación de Ollama🦙
1. Instalar [Ollama](https://ollama.com/) en el servidor.

2. Descarga los modelos que quieras usar, en este caso
```bash
ollama run gemma2 # LLM principal para tareas
ollama run llava # Para tareas como reconocimiento de imágenes
ollama pull nextfire/paraphrase-multilingual-minilm # modelo de Embedding
```

3. En `config.py` establece `OLLAMA_CHAT`, `OLLAMA_VISUAL_CHAT`, y `OLLAMA_EMBEDDINGS_MODEL` Los modelos que has descargado en ollama y quieres utilizar.

### Instalación y despliegue con Docker.  🐳 

1. Instalar [Docker](https://www.docker.com/products/docker-desktop/) en el servidor.

2. Desde la carpeta Sirillama ejecutamos los siguientes comentos

```bash
docker build -t sirillama .
docker run -d --name sirillamabeta --restart always -p 5001:5001 sirillama
```

Desde el log debería aparecerte algo similar

```bash
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://192.168.1.134:5001
Press CTRL+C to quit
```
## Ajustes
En `confing.py` establece `MEMORY_SIZE` (Los mensajes anteriores a recordar) and `ANSWER_SIZE_WORDS` (Cuantas palabras quiere que contenga la respuesta)

## Ejecutando SiriLlama en tu dispositivo Apple 🟣🦙

4. En tu dispositivo Apple, descarga el siguiente atajo [aquí](https://www.icloud.com/shortcuts/fd032a4e75cc4d81a6f9a742053d4c18).
Ten en cuenta que, para “hablar” con él, debes ejecutar el atajo a través de Siri; de lo contrario, se te solicitará que escribas el texto.

5. Ejecuta el atajo a través de Siri o de la interfaz del propio atajo. La primera vez que lo ejecutes, se te pedirá que introduzcas tu [dirección IP](https://stackoverflow.com/a/15864222) y el número de puerto que aparece en la terminal.

En el ejemplo anterior, la dirección IP es `192.168.1.134` y el puerto es `5001` (Es el puerto predeterminado, puedes cambiarlo si fuera necesario desde main.py).

6. Si estás usando Siri para interactuar con el atajo, decir “Adiós” detendrá a Siri.


# Otros modelos LLM 🤖🤖
Supuestamente, SiriLLama debería funcionar con cualquier LLM, incluidos OpenAI, Claude, etc. Pero asegúrate primero de haber instalado los paquetes correspondientes de Langchain y de configurar los modelos en... `config.py`

# SiriLLama en redes públicas. 🌎
- Es posible ejecutar Siri ollama sin estar en la red local a través de VPN como [Wireguard](https://www.wireguard.com/) o similares.

# Tips 💡💡
- Para usar la función multimodal, solo es posible con imágenes que no estén en formato HEIF. Puedes cambiar esto en la configuración de tu cámara (no afectará a tus fotos existentes). En la sección de formatos, elige “Más compatible” ¡y listo!
