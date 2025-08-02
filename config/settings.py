import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    WEAVIATE_URL = os.getenv("WEAVIATE_URL", "http://localhost:8080")
    WEAVIATE_API_KEY = os.getenv("WEAVIATE_API_KEY", "")
    EMBEDDING_MODEL = "text-embedding-ada-002"
    LLM_MODEL = "gpt-3.5-turbo"
    VAPI_API_KEY = os.getenv("VAPI_API_KEY")

settings = Settings()
