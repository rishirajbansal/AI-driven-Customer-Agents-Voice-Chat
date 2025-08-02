from fastapi import APIRouter
from app.agents.support_agent import handle_customer_query

router = APIRouter()

@router.get("/ask")
def ask_agent(q: str):
    response = handle_customer_query(q)
    return {"response": response}
