from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import basicsynbio as bsb
from pathlib import Path
import os
from app.schema import (
    fileType,
    fileTypeData,
    basicBuild,
    basicPart,
    responseCollectionsName,
    responseCollectionsData,
)
from typing import List

from app.src.getCollections import getCollections
from app.src.fileUploadSingular import fileUploadSingular
from app.src.fileUploadMultiple import fileUploadMultiple
from app.src.buildCSVs import buildCSVs
from app.src.buildEchoInstructions import buildEchoInstructions
from app.src.buildPDFInstructions import buildPDFInstructions
from app.src.buildJSON import buildJSON
from app.src.buildUniqueParts import buildUniqueParts
from app.src.buildUniqueAssemblies import buildUniqueAssemblies
from app.src.validateAssembly import validateAssembly
from app.src.viewseqlabels import viewseqlabels
from app.src.viewpartlabels import viewpartlabels
from app.src.return_sequence_annotations import return_sequence_annotations
from app.src.dnafeatureviewer import dnafeaturesviewerpng
from app.src.dnafeatureviewer_assembly import dnafeaturesviewerpng_assembly

description = """
A REST API for BasicSynBio that allows the BasicSynBio python package to be consumed by any language - the primary use case for this is own own BasicSynBio frontend application. 🚀

[Python Package](https://pypi.org/project/basicsynbio/) --- 
[Interactive Web App](https://basicsynbio.web.app)

Below is a list of endpoints that can be accessed via the API, each endpoint can be simulated within their corresponding boxes.
"""

app = FastAPI(
    title="BasicSynBio API",
    description=description,
    version="0.0.1",
)

origins = [
    "http://basicsynbio.web.app",
    "https://basicsynbio.web.app",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# the `/docs` endpoint is reserved for OPENAPI good for testing
# Root to the API to check if it is running
@app.get("/")
def root_endpoint_for_health_check():
    """
    ## API Root

    Root endpoint for health check, returns basic message.
    """
    return {"message": "Hello World"}


# Route to return the available collections
@app.get("/collections/names", response_model=responseCollectionsName)
def get_collection_names():
    """
    ## Collection Names

    Returns a list of the available basicynbio part collections to the user.

    More infomation about part linker collections can be found at the [basicsynbio documentation](https://londonbiofoundry.github.io/basicsynbio/collections.html)
    """
    return {"data": [x for x in dir(bsb) if x.startswith("BASIC_")]}


# Route to return data within available collections
@app.get("/collections/data", response_model=responseCollectionsData)
def get_collection_data():
    """
    ## Collection Data

    Returns a list of the available basicynbio part collections and the data within them to the user.

    More infomation about part linker collections can be found at the [basicsynbio documentation](https://londonbiofoundry.github.io/basicsynbio/collections.html)
    """
    return {"data": getCollections()}


# Route to return sequence data witin a uploaded file
@app.post("/fileupload/singular")
def singular_file_upload(
    type: fileType, addiseq: bool, file: UploadFile = File(...)
):
    """
    ## Singular File Upload

    Uploads a file containing only one sequence record to the server to return a JSON version of the same object for further processing in the basicsynbio interactive web app.
    """
    return fileUploadSingular(type, addiseq, file)


# Route to return sequence datas for each record within a uploaded file
@app.post("/fileupload/multiple")
async def multiple_file_upload(
    type: fileType, addiseq: bool, file: UploadFile = File(...)
):
    """
    ## Multiple File Upload

    Uploads a file containing more than one sequence record to the server to return a JSON version of the same object for further processing in the basicsynbio interactive web app.
    """
    return await fileUploadMultiple(type, addiseq, file)


# Route to return CSV representation on basicBuild Object
@app.post("/buildcsvs")
async def build_csvs(myBuild: List[basicBuild]):
    """
    ## Build CSVs

    This endpoint takes a list of basicBuild objects and returns a CSV representation of the same objects.
    """
    return buildCSVs(myBuild)


# Route to return echo representation on basicBuild Object
@app.post("/buildechoinstructions")
async def build_echo_instructions(myBuild: List[basicBuild]):
    """
    ## Build Echo Instructions

    This endpoint takes a list of basicBuild objects and returns the Echo robot instructions to perform the clip step of BASIC DNA assembly.
    """
    return buildEchoInstructions(myBuild)


# Route to return PDF representation on basicBuild Object
@app.post("/build_pdf_instructions")
async def build_pdf_instructions(myBuild: List[basicBuild]):
    """
    ## Build PDF Instructions

    This endpoint takes a list of basicBuild objects and returns a PDF for the manual assembly within a lab of the BasicBuild object.
    """
    return buildPDFInstructions(myBuild)


# Route to return JSON representation on basicBuild Object
@app.post("/buildjson")
async def build_json(myBuild: List[basicBuild]):
    """
    ## Build JSON

    This endpoint takes a list of basicBuild objects and returns a JSON serialised version of the same objects.
    """
    return buildJSON(myBuild)


# Route to return unique assemblies genbank representation on basicBuild Object
@app.post("/builduniqueparts")
async def build_unique_parts_as_genbank(myBuild: List[basicBuild]):
    """
    ## Build Unique Parts

    This endpoint takes a list of basicBuild objects and returns unique parts within each BasicAssembly as a genbank file.
    """
    return buildUniqueParts(myBuild)


# Route to return unique assemblies genbank representation on basicBuild Object
@app.post("/builduniqueassemblies")
async def buils_unique_assemblies_as_genbank(myBuild: List[basicBuild]):
    """
    ## Build Unique Assemblies

    This endpoint takes a list of basicBuild objects and returns unique assemblies within the BasicBuild as a genbank file.
    """
    return buildUniqueAssemblies(myBuild)


# Route to return unique assemblies genbank representation on basicBuild Object
@app.post("/validate")
async def validate_assembly(myBuild: List[basicPart]):
    """
    ## Validate

    This endpoint ensures that a input list of basicParts can successfully build a basic assembly.
    """
    return validateAssembly(myBuild)


#################### Visualization ####################

# Route to return unique assemblies seq labels representation of basicBuild Object
@app.post("/viewseqlabels")
async def view_sequence_labels(myBuild: List[basicPart]):
    return viewseqlabels(myBuild)


# Route to return unique assemblies part labels representation of basicBuild Object
@app.post("/viewpartlabels")
async def view_part_labels(myBuild: basicPart):
    return viewpartlabels(myBuild)


# Route to return sequence annotations
@app.post("/returnseqann")
async def view_sequence_annotations(myBuild: basicPart, Qualifier: str):
    return return_sequence_annotations(myBuild, Qualifier)


# Route to return sequence annotations
@app.post("/dnafeatureviewer")
async def dnafeatureviewer(myBuild: basicPart):
    return dnafeaturesviewerpng(myBuild)


# Route to return sequence annotations for assemblys on Dna feature viewer
@app.post("/dnafeatureviewer_assembly")
async def dnafeaturesviewer_for_assemblies(myBuild: List[basicPart]):
    return dnafeaturesviewerpng_assembly(myBuild)
