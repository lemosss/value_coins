from typing import Generator

import pytest
from fastapi.testclient import TestClient

from database.test_db import Base, engine, override_get_db
from main import app, get_db

Base.metadata.create_all(bind=engine)

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
