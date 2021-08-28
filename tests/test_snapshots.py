from fastapi.testclient import TestClient
from snapshottest.file import FileSnapshot

from app.main import app

client = TestClient(app)

def test_root_hello_world(snapshot):
    """Testing the API for root"""
    my_api_response = client.get("/")
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())


def test_collection_names(snapshot):
    """Testing the API for root"""
    my_api_response = client.get("/collections/names")
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())

def test_collection_data(snapshot):
    """Testing the API for root"""
    my_api_response = client.get("/collections/data")
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())