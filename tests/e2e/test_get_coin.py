from fastapi.testclient import TestClient


class TestGetCoin:
    def test_get_dollar(self, client: TestClient):
        response = client.get("/api/coins/dollar")
        assert response.status_code == 200
        data = response.json()
        assert type(data["dollar_value"]) is float

    def test_get_euro(self, client: TestClient):
        response = client.get("/api/coins/euro")
        assert response.status_code == 200
        data = response.json()
        assert type(data["euro_value"]) is float
