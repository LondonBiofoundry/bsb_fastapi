from fastapi.testclient import TestClient
from snapshottest.file import FileSnapshot
from pathlib import Path
import json

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

    ############### FASTA file upload ###############

    # Test for adding a file successfully that needs i seq
    # This is how you add query parameters to the URL to make a request
    _params = {"type": "fasta", "addiseq": "true"}
    # This is how you add a file to the request to simulate a upload File input
    my_api_response = client.post(
        "/fileupload/singular",
        params=_params,
        files={
            "file": (
                "filename",
                open("tests/inputs/single-sfgfp.fasta", "rb"),
                "application/fasta",
            )
        },
    )
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())

    # Test for adding a file unsuccessfully that needs i seq

    _params = {"type": "fasta", "addiseq": "false"}
    my_api_response = client.post(
        "/fileupload/singular",
        params=_params,
        files={
            "file": (
                "filename",
                open("tests/inputs/single-sfgfp.fasta", "rb"),
                "application/fasta",
            )
        },
    )
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())

    ################## Genbank file upload ##################

    _params = {"type": "genbank", "addiseq": "true"}
    # This is how you add a file to the request to simulate a upload File input
    my_api_response = client.post(
        "/fileupload/singular",
        params=_params,
        files={
            "file": (
                "filename",
                open("tests/inputs/single-sfgfp.gb", "rb"),
                "application/fasta",
            )
        },
    )
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())

    # Test for adding a file unsuccessfully that needs i seq

    _params = {"type": "genbank", "addiseq": "false"}
    my_api_response = client.post(
        "/fileupload/singular",
        params=_params,
        files={
            "file": (
                "filename",
                open("tests/inputs/single-sfgfp.gb", "rb"),
                " chemical/seq-na-genbank",
            )
        },
    )
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())


def test_singular_build_csvs(snapshot):
    """Testing the API for ability to build csv"""
    f = open("tests/inputs/BasicBuild.json")
    _data = json.load(f)
    my_api_response = client.post(
        "/buildcsvs",
        json=_data,
    )
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.content)
