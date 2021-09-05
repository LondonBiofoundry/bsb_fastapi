from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import basicsynbio as bsb
from pathlib import Path
import os
from app.schema import fileType, fileTypeData, basicBuild, basicPart
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
def root():
    return {"message": "Hello World"}


# Route to return the available collections
@app.get("/collections/names")
def getCollectionsNames():
    return {"data": [x for x in dir(bsb) if x.startswith("BASIC_")]}


# Route to return data within available collections
@app.get("/collections/data")
def getCollectionsData():
    return {"data": getCollections()}


# Route to return sequence data witin a uploaded file
@app.post("/fileupload/singular")
async def file_upload_singular(
    type: fileType, addiseq: bool, file: UploadFile = File(...)
):
    return await fileUploadSingular(type, addiseq, file)


# Route to return sequence datas for each record within a uploaded file
@app.post("/fileupload/multiple")
async def file_upload_multiple(
    type: fileType, addiseq: bool, file: UploadFile = File(...)
):
    return await fileUploadMultiple(type, addiseq, file)


# Route to return CSV representation on basicBuild Object
@app.post("/buildcsvs")
async def return_build_csvs(myBuild: List[basicBuild]):
    return buildCSVs(myBuild)


# Route to return echo representation on basicBuild Object
@app.post("/buildechoinstructions")
async def return_build_echo_instructions(myBuild: List[basicBuild]):
    return buildEchoInstructions(myBuild)


# Route to return PDF representation on basicBuild Object
@app.post("/build_pdf_instructions")
async def return_build_pdf_instructions(myBuild: List[basicBuild]):
    return buildPDFInstructions(myBuild)


# Route to return JSON representation on basicBuild Object
@app.post("/buildjson")
async def return_build_json(myBuild: List[basicBuild]):
    return buildJSON(myBuild)


# Route to return unique assemblies genbank representation on basicBuild Object
@app.post("/builduniqueparts")
async def return_unique_parts_genbank(myBuild: List[basicBuild]):
    return buildUniqueParts(myBuild)


# Route to return unique assemblies genbank representation on basicBuild Object
@app.post("/builduniqueassemblies")
async def return_unique_assemblies_genbank(myBuild: List[basicBuild]):
    return buildUniqueAssemblies(myBuild)


# Route to return unique assemblies genbank representation on basicBuild Object
@app.post("/validate")
async def return_validate_assembly(myBuild: List[basicPart]):
    return validateAssembly(myBuild)


#################### Visualization ####################

# Route to return unique assemblies seq labels representation of basicBuild Object
@app.post("/viewseqlabels")
async def return_seq_labels(myBuild: List[basicPart]):
    return viewseqlabels(myBuild)


# Route to return unique assemblies part labels representation of basicBuild Object
@app.post("/viewpartlabels")
async def return_part_labels(myBuild: basicPart):
    return viewpartlabels(myBuild)


# Route to return sequence annotations
@app.post("/returnseqann")
async def return_seq_annotations(myBuild: basicPart, Qualifier: str):
    return return_sequence_annotations(myBuild, Qualifier)


# Route to return sequence annotations
@app.post("/dnafeatureviewer")
async def return_dnafeatureviewer(myBuild: basicPart):
    return dnafeaturesviewerpng(myBuild)


# Route to return sequence annotations for assemblys on Dna feature viewer
@app.post("/dnafeatureviewer_assembly")
async def returndnafeaturesviewer_assembly(myBuild: List[basicPart]):
    return dnafeaturesviewerpng_assembly(myBuild)
