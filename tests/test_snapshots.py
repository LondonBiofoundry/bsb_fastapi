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


def test_validate_success_without_files(snapshot):
    """Testing the API for ability to validate builds"""
    f = open("tests/inputs/validatePass/Passing.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    my_api_response = client.post(
        "/validate", data={"myPartArrayStr": _dataString}, files={}
    )
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())


def test_validate_success_with_files(snapshot):
    """Testing the API for ability to validate builds"""
    f = open("tests/inputs/validatePass/PassingWithFiles.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    seva12path = "tests/inputs/validatePass/SEVA_12.gb"
    seva13path = "tests/inputs/validatePass/SEVA_13.gb"
    myFiles = [
        ("files", ("SEVA_12.gb", open(seva12path, "rb"))),
        ("files", ("SEVA_13.gb", open(seva13path, "rb"))),
    ]
    print(myFiles)
    my_api_response = client.post(
        "/validate",
        data={"myPartArrayStr": _dataString},
        files=myFiles,
    )
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())


def test_validate_fail_without_files(snapshot):
    """Testing the API for ability to validate builds"""
    f = open("tests/inputs/validateFail/Failing.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    my_api_response = client.post(
        "/validate", data={"myPartArrayStr": _dataString}, files={}
    )
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())


def test_validate_fail_with_files(snapshot):
    """Testing the API for ability to validate builds"""
    f = open("tests/inputs/validateFail/FailingWithFiles.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    seva12path = "tests/inputs/validateFail/SEVA_12.gb"
    seva13path = "tests/inputs/validateFail/SEVA_13.gb"
    myFiles = [
        ("files", ("SEVA_12.gb", open(seva12path, "rb"))),
        ("files", ("SEVA_13.gb", open(seva13path, "rb"))),
    ]
    print(myFiles)
    my_api_response = client.post(
        "/validate",
        data={"myPartArrayStr": _dataString},
        files=myFiles,
    )
    snapshot.assert_match(my_api_response.status_code)
    snapshot.assert_match(my_api_response.json())


def test_singular_build_csvs(snapshot):
    """Testing the API for ability to build csv"""
    f = open("tests/inputs/basicBuildExamples/simple1AssemblyArray.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    my_api_response = client.post(
        "/buildcsvs", data={"myAssemblyArrayStr": _dataString}, files={}
    )
    snapshot.assert_match(my_api_response.status_code)
    # TODO: fix snapshot of binary zip response containing 2 csv files
    # snapshot.assert_match(my_api_response.content)


def test_singular_build_csvs_with_files(snapshot):
    """Testing the API for ability to build csv"""
    f = open("tests/inputs/basicBuildExamples/simple1AssemblyArray.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    seva12path = "tests/inputs/validateFail/SEVA_12.gb"
    seva13path = "tests/inputs/validateFail/SEVA_13.gb"
    myFiles = [
        ("files", ("SEVA_12.gb", open(seva12path, "rb"))),
        ("files", ("SEVA_13.gb", open(seva13path, "rb"))),
    ]
    my_api_response = client.post(
        "/buildcsvs", data={"myAssemblyArrayStr": _dataString}, files=myFiles
    )
    snapshot.assert_match(my_api_response.status_code)
    # TODO: fix snapshot of binary zip response containing 2 csv files
    # snapshot.assert_match(my_api_response.content)


def test_singular_build_echoinstructions(snapshot):
    """Testing the API for ability to build csv"""
    f = open("tests/inputs/basicBuildExamples/simple1AssemblyArray.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    my_api_response = client.post(
        "/buildechoinstructions", data={"myAssemblyArrayStr": _dataString}, files={}
    )
    snapshot.assert_match(my_api_response.status_code)
    # TODO: fix snapshot of binary zip response containing 2 csv files
    # snapshot.assert_match(my_api_response.content)


def test_singular_build_echoinstructions_with_files(snapshot):
    """Testing the API for ability to build csv"""
    f = open("tests/inputs/basicBuildExamples/simple1AssemblyArray.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    seva12path = "tests/inputs/validateFail/SEVA_12.gb"
    seva13path = "tests/inputs/validateFail/SEVA_13.gb"
    myFiles = [
        ("files", ("SEVA_12.gb", open(seva12path, "rb"))),
        ("files", ("SEVA_13.gb", open(seva13path, "rb"))),
    ]
    my_api_response = client.post(
        "/buildechoinstructions",
        data={"myAssemblyArrayStr": _dataString},
        files=myFiles,
    )
    snapshot.assert_match(my_api_response.status_code)
    # TODO: fix snapshot of binary zip response containing 2 csv files
    # snapshot.assert_match(my_api_response.content)


def test_singular_build_pdf(snapshot):
    """Testing the API for ability to build csv"""
    f = open("tests/inputs/basicBuildExamples/simple1AssemblyArray.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    my_api_response = client.post(
        "/build_pdf_instructions", data={"myAssemblyArrayStr": _dataString}, files={}
    )
    snapshot.assert_match(my_api_response.status_code)
    # TODO: fix snapshot of binary zip response containing 2 csv files
    # snapshot.assert_match(my_api_response.content)


def test_singular_build_pdf_with_files(snapshot):
    """Testing the API for ability to build csv"""
    f = open("tests/inputs/basicBuildExamples/simple1AssemblyArray.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    seva12path = "tests/inputs/validateFail/SEVA_12.gb"
    seva13path = "tests/inputs/validateFail/SEVA_13.gb"
    myFiles = [
        ("files", ("SEVA_12.gb", open(seva12path, "rb"))),
        ("files", ("SEVA_13.gb", open(seva13path, "rb"))),
    ]
    my_api_response = client.post(
        "/build_pdf_instructions",
        data={"myAssemblyArrayStr": _dataString},
        files=myFiles,
    )
    snapshot.assert_match(my_api_response.status_code)
    # TODO: fix snapshot of binary zip response containing 2 csv files
    # snapshot.assert_match(my_api_response.content)


def test_singular_build_json(snapshot):
    """Testing the API for ability to build csv"""
    f = open("tests/inputs/basicBuildExamples/simple1AssemblyArray.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    my_api_response = client.post(
        "/buildjson", data={"myAssemblyArrayStr": _dataString}, files={}
    )
    snapshot.assert_match(my_api_response.status_code)
    # TODO: fix snapshot of binary zip response containing 2 csv files
    snapshot.assert_match(my_api_response.json())


def test_singular_build_json_with_files(snapshot):
    """Testing the API for ability to build csv"""
    f = open("tests/inputs/basicBuildExamples/simple1AssemblyArray.json")
    _data = json.load(f)
    _dataString = json.dumps(_data)
    seva12path = "tests/inputs/validateFail/SEVA_12.gb"
    seva13path = "tests/inputs/validateFail/SEVA_13.gb"
    myFiles = [
        ("files", ("SEVA_12.gb", open(seva12path, "rb"))),
        ("files", ("SEVA_13.gb", open(seva13path, "rb"))),
    ]
    my_api_response = client.post(
        "/buildjson",
        data={"myAssemblyArrayStr": _dataString},
        files=myFiles,
    )
    snapshot.assert_match(my_api_response.status_code)
    # TODO: fix snapshot of binary zip response containing 2 csv files
    snapshot.assert_match(my_api_response.json())


# def test_collection_data(snapshot):
#     """Testing the API for collection data"""
#     my_api_response = client.get("/collections/data")
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())


# def test_singular_file_upload(snapshot):
#     """Testing the API for ability to upload singular files"""

#     ############### FASTA file upload ###############

#     # Test for adding a file successfully that needs i seq
#     # This is how you add query parameters to the URL to make a request
#     _params = {"type": "fasta", "addiseq": "true"}
#     # This is how you add a file to the request to simulate a upload File input
#     my_api_response = client.post(
#         "/fileupload/singular",
#         params=_params,
#         files={
#             "file": (
#                 "single-sfgfp.fasta",
#                 open("tests/inputs/single-sfgfp.fasta", "rb"),
#                 "application/fasta",
#             )
#         },
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())

#     # Test for adding a file unsuccessfully that needs i seq

#     _params = {"type": "fasta", "addiseq": "false"}
#     my_api_response = client.post(
#         "/fileupload/singular",
#         params=_params,
#         files={
#             "file": (
#                 "single-sfgfp.fasta",
#                 open("tests/inputs/single-sfgfp.fasta", "rb"),
#                 "application/fasta",
#             )
#         },
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())

#     ################## Genbank file upload ##################

#     _params = {"type": "genbank", "addiseq": "true"}
#     # This is how you add a file to the request to simulate a upload File input
#     my_api_response = client.post(
#         "/fileupload/singular",
#         params=_params,
#         files={
#             "file": (
#                 "single-sfgfp.gb",
#                 open("tests/inputs/single-sfgfp.gb", "rb"),
#                 "application/fasta",
#             )
#         },
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())

#     # Test for adding a file unsuccessfully that needs i seq

#     _params = {"type": "genbank", "addiseq": "false"}
#     my_api_response = client.post(
#         "/fileupload/singular",
#         params=_params,
#         files={
#             "file": (
#                 "single-sfgfp.gb",
#                 open("tests/inputs/single-sfgfp.gb", "rb"),
#                 "chemical/seq-na-genbank",
#             )
#         },
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())


# def test_singular_build_csvs(snapshot):
#     """Testing the API for ability to build csv"""
#     f = open("tests/inputs/basicAssembly.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/buildcsvs",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     # TODO: fix snapshot of binary zip response containing 2 csv files
#     # snapshot.assert_match(my_api_response.raw)


# def test_singular_build_echo_instructions(snapshot):
#     """Testing the API for ability to build echo instructions"""
#     f = open("tests/inputs/basicAssembly.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/buildechoinstructions",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     # TODO: fix snapshot of binary zip response containing 2 csv files
#     # snapshot.assert_match(my_api_response.raw)


# def test_singular_build_PDF_instructions(snapshot):
#     """Testing the API for ability to pdf instructions"""
#     f = open("tests/inputs/basicAssembly.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/build_pdf_instructions",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     # TODO: fix snapshot of binary zip response containing 2 csv files
#     # snapshot.assert_match(my_api_response.raw)


# def test_singular_build_json(snapshot):
#     """Testing the API for ability to json instructions"""
#     f = open("tests/inputs/basicAssembly.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/buildjson",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     # TODO: fix snapshot of binary zip response containing 2 csv files
#     # snapshot.assert_match(my_api_response.raw)


# def test_singular_unique_parts_genbank(snapshot):
#     """Testing the API for ability to build unique parts genbank"""
#     f = open("tests/inputs/basicAssembly.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/builduniqueparts",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     # TODO: fix snapshot of binary zip response containing 2 csv files
#     # snapshot.assert_match(my_api_response.raw)


# def test_singular_unique_assemblies_genbank(snapshot):
#     """Testing the API for ability to build unique assemblies genbank"""
#     f = open("tests/inputs/basicAssembly.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/builduniqueassemblies",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     # TODO: fix snapshot of binary zip response containing 2 csv files
#     # snapshot.assert_match(my_api_response.raw)


# def test_validate_success(snapshot):
#     """Testing the API for ability to validate builds"""
#     f = open("tests/inputs/basicAssemblyPartsValidate.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/validate",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())


# def test_validate_failure(snapshot):
#     """Testing the API for ability to fail builds"""
#     f = open("tests/inputs/basicAssemblyPartsFailure.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/validate",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())


# def test_get_seq_labels(snapshot):
#     """Testing the API for ability to return seq labels"""
#     f = open("tests/inputs/basicAssemblyPartsValidate.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/viewseqlabels",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())


# def test_get_part_labels(snapshot):
#     """Testing the API for ability to return part labels"""
#     f = open("tests/inputs/BasicPartSeva14.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/viewpartlabels",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())


# def test_get_part_labels(snapshot):
#     """Testing the API for ability to return part labels"""
#     f = open("tests/inputs/BasicPartSeva14.json")
#     _data = json.load(f)
#     _params = {"Qualifier": "label"}
#     my_api_response = client.post(
#         "/returnseqann",
#         params=_params,
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())


# def test_dna_feature_viewer(snapshot):
#     """Testing the API for ability to return part labels"""
#     f = open("tests/inputs/BasicPartSeva14.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/dnafeatureviewer",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())


# def test_dna_feature_viewer_assembly(snapshot):
#     """Testing the API for ability to return part labels"""
#     f = open("tests/inputs/basicAssemblyPartsValidate.json")
#     _data = json.load(f)
#     my_api_response = client.post(
#         "/dnafeatureviewer_assembly",
#         json=_data,
#     )
#     snapshot.assert_match(my_api_response.status_code)
#     snapshot.assert_match(my_api_response.json())
