from fastapi import File, UploadFile
import basicsynbio as bsb
from app.schema import fileType, fileTypeData

from app.utils.basicPartFromFile import returnBasicPartFromUploadFile


async def fileUploadSingular(
    type: fileType, addiseq: bool, file: UploadFile = File(...)
):
    return returnBasicPartsFromUploadFile(file, type, addiseq)
