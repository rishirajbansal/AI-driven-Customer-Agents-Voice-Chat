from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_agent():
    response = client.get("/ask?q=Hello")
    assert response.status_code == 200
    assert "response" in response.json()
