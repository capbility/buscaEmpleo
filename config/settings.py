import os
from dotenv import load_dotenv
from pydantic import SecretStr

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_GEMINI = os.getenv("MODEL_GEMINI")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_OPENAI = os.getenv("MODEL_OPENAI")

if GEMINI_API_KEY and MODEL_GEMINI:
    PROVIDER = "gemini"
    API_KEY = SecretStr(GEMINI_API_KEY)
    MODEL = MODEL_GEMINI
elif OPENAI_API_KEY and MODEL_OPENAI:
    PROVIDER = "openai"
    API_KEY = SecretStr(OPENAI_API_KEY)
    MODEL = MODEL_OPENAI
else:
    raise ValueError("No se encontró ninguna configuración válida de modelo. Define las variables en el .env.")
