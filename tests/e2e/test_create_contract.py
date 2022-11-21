from fastapi.testclient import TestClient


class TestCreateContract:
    def test_create_contract(self, client: TestClient):
        data = {"name": "Lemos", "email": "test@test.com", "tel": 996877245}
        response = client.post("/api/contacts", json=data)
        assert response.status_code == 201, response.text
        data = response.json()
        assert data["name"] == "Lemos"
        assert data["email"] == "test@test.com"
        assert data["tel"] == 996877245

    def test_create_contract_invalid_payload(self, client: TestClient):
        data = {"name": "Lemos", "tel": 0}
        response = client.post("/api/contacts", json=data)
        assert response.status_code == 422, response.text
