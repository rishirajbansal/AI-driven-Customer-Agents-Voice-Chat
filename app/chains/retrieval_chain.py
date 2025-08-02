from app.db.weaviate_client import similarity_search
from app.services.llm_interface import generate_response

def retrieval_augmented_response(query):
    docs = similarity_search(query)
    context = "\n".join(docs)
    prompt = f"Given the following support context:\n{context}\nAnswer: {query}"
    return generate_response(prompt)
