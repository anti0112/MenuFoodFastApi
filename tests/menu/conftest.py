import pytest
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from starlette.testclient import TestClient
from starlette.requests import Request
from menu.models import Base
from core.utils import get_db
from core.db import SQLALCHEMY_DATABASE_URL
from main import app


engine = create_engine(SQLALCHEMY_DATABASE_URL)
database_exists = database_exists(engine.url)
if not database_exists:
    create_database(engine.url)


def override_get_db(request:Request):
    return request.state.db


@pytest.fixture(scope="class")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="class")
def test_client():
    with TestClient(app) as client:
        yield client