from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import basicsynbio as bsb
from pathlib import Path
import os
from app.schema import fileType, fileTypeData, basicBuild
from typing import List

from app.src.getCollections import getCollections
from app.src.fileUploadSingular import fileUploadSingular
from app.src.fileUploadMultiple import fileUploadMultiple
from app.src.buildCSVs import buildCSVs
from app.src.buildEchoInstructions import buildEchoInstructions
from app.src.buildPDFInstructions import buildPDFInstructions
from app.src.buildJSON import buildJSON


app = FastAPI()

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
