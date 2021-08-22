from fastapi import FastAPI, File, UploadFile
import basicsynbio as bsb
from pathlib import Path
import os
from app.schema import fileType, fileTypeData

from app.src.getCollections import getCollections
from app.src.fileUploadSingular import fileUploadSingular

app = FastAPI()

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


@app.post("/fileupload/singular")
async def file_upload_singular(
    type: fileType, addiseq: bool, file: UploadFile = File(...)
):
    return await fileUploadSingular(type, addiseq, file)


@app.post("/fileupload/multiple")
async def file_upload_multiple(
    type: fileType, addiseq: bool, file: UploadFile = File(...)
):
    return await fileUploadMultiple(type, addiseq, file)
