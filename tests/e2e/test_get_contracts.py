from fastapi.testclient import TestClient


class TestGetContract:
    def test_get_one_contract(self, client: TestClient):
        data = {"name": "Lemos", "email": "test@test.com", "tel": "996877245"}
        response = client.post("/api/contacts", json=data)
        assert response.status_code == 201, response.text

        response = client.get("/api/contacts/1")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "Lemos"
        assert data["email"] == "test@test.com"
        assert data["tel"] == "996877245"

    def test_get_all_contracts(self, client: TestClient):
        data = {"name": "Lemos", "email": "test@test.com", "tel": "996877245"}
        response = client.post("/api/contacts", json=data)

        response = client.get("/api/contacts")
        assert response.status_code == 200
        data = response.json()
        assert data[0]["name"] == "Lemos"
        assert data[0]["email"] == "test@test.com"
        assert data[0]["tel"] == "996877245"
