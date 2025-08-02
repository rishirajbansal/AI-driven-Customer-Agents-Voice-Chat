import weaviate
from config.settings import settings

client = weaviate.Client(
    url=settings.WEAVIATE_URL,
    additional_headers={
        "X-OpenAI-Api-Key": settings.OPENAI_API_KEY
    }
)

def create_schema():
    if not client.schema.contains({"class": "SupportDocs"}):
        schema = {
            "classes": [{
                "class": "SupportDocs",
                "description": "Customer support content",
                "vectorizer": "text2vec-openai",
                "properties": [{
                    "name": "content",
                    "dataType": ["text"]
                }]
            }]
        }
        client.schema.create(schema)

def upload_documents(docs):
    with client.batch as batch:
        for doc in docs:
            batch.add_data_object({
                "content": doc
            }, "SupportDocs")

def similarity_search(query, top_k=3):
    result = client.query.get("SupportDocs", ["content"]) \
        .with_near_text({"concepts": [query]}) \
        .with_limit(top_k) \
        .do()
    return [res['content'] for res in result['data']['Get']['SupportDocs']]
