from langchain.chat_models import ChatOpenAI
from config.settings import settings

llm = ChatOpenAI(model_name=settings.LLM_MODEL, openai_api_key=settings.OPENAI_API_KEY)

def generate_response(prompt):
    return llm.predict(prompt)
