from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_status():
    """Unit Test: Verifies the API root endpoint is reachable."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the IBM Candidate Task API"}

def test_get_tasks():
    """Unit Test: Verifies the task list retrieval."""
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)