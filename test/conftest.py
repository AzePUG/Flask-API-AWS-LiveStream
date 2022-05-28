import pytest
import uuid
from src.entrypoints.api.app import create_app


@pytest.fixture
def app():
    return create_app("testing")

@pytest.fixture
def get_uuid():
    return uuid.uuid4()

@pytest.fixture
def get_init_jpg_dict(get_uuid):
   return {
        "code": get_uuid,
        "src_path": "fake.jpg"
    }
   
@pytest.fixture
def get_init_pdf_dict(get_uuid):
    return {
        "code": get_uuid,
        "dest_path": "fake.pdf"
    }