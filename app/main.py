from fastapi import FastAPI
from app.endpoints.routes import router
from app.db.weaviate_client import create_schema

app = FastAPI(title="AI Support Agent")
app.include_router(router)

@app.on_event("startup")
def startup():
    create_schema()
