from fastapi.testclient import TestClient
from snapshottest.file import FileSnapshot
from pathlib import Path
from app.main import app

client = TestClient(app)


def test_root_hello_world(snapshot):
    """Testing the API for root"""
    my_api_response = client.get("/")
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())


def test_collection_names(snapshot):
    """Testing the API for collection names"""
    my_api_response = client.get("/collections/names")
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())


def test_collection_data(snapshot):
    """Testing the API for collection data"""
    my_api_response = client.get("/collections/data")
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())


def test_singular_file_upload(snapshot):
    """Testing the API for ability to upload singular files"""
    # This is how you add query parameters to the URL to make a request
    _params={'type':'fasta','addiseq':'true'}
    # This is how you add a file to the request to simulate a upload File input
    my_api_response = client.post(
        "/fileupload/singular",
        params=_params,
        files={"file": ("filename", open("tests/inputs/single-sfgfp.fasta", "rb"),"application/fasta")},
    )
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())
