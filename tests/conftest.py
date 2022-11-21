import sys
from typing import Generator

import pytest
from fastapi.testclient import TestClient

from database.test_database import Base, engine, override_get_db
from main import app, get_db

sys.path.append("...")

Base.metadata.create_all(bind=engine)

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
