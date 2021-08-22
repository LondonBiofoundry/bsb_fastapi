from fastapi import File, UploadFile
import basicsynbio as bsb
from app.schema import fileType, fileTypeData

from app.utils.basicPartFromFile import basicPartsFromUploadFile


async def fileUploadMultiple(
    type: fileType, addiseq: bool, file: UploadFile = File(...)
):
    return basicPartsFromUploadFile(file, type, addiseq)
