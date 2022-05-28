import pytest
import uuid
from src.entrypoints.api.app import create_app


@pytest.fixture
def app():
    return create_app("testing")

@pytest.fixture
def get_uuid():
    return uuid.uuid4()