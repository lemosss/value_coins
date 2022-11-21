import sys

from fastapi.testclient import TestClient

sys.path.append("...")


class TestHealthCheck:
    def test_heath_check(self, client: TestClient):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"status": "OK"}
