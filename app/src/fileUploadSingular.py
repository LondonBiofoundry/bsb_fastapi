from fastapi import File, UploadFile
import basicsynbio as bsb
from app.schema import fileType, fileTypeData

from app.utils.basicPartFromFile import returnBasicPartFromUploadFile


async def fileUploadSingular(
    type: fileType, addiseq: bool, file: UploadFile = File(...)
):
    result = returnBasicPartFromUploadFile(file, type, addiseq)
    if isinstance(result, bsb.BasicPart):
        return {
            "file_size": file.filename,
            "typeData": fileTypeData[type],
            "type": type,
            "addiseq": addiseq,
            "fileb_content_type": file.content_type,
        }
    else:
        return result
