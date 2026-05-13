from app import app

def test_index():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Backend API is running"

def test_post_requires_title():
    client = app.test_client()
    response = client.post("/api/data", json={})
    assert response.status_code == 400
    assert response.get_json()["error"] == "title is required"
