from fastapi import File, UploadFile
import basicsynbio as bsb
from app.schema import basicPartType, fileType, fileTypeData

from app.utils.basicPartFromFile import returnBasicPartFromUploadFileInitial
from app.utils.bsbBasicPartToJsonbasicPart import bsbBasicPartToJsonbasicPart


def fileUploadSingular(type: fileType, addiseq: bool, file: UploadFile = File(...)):
    result = returnBasicPartFromUploadFileInitial(file, type, addiseq)
    if isinstance(result, bsb.BasicPart):
        jsonBasicPart = bsbBasicPartToJsonbasicPart(
            result, basicPartType.uploadSingle, file
        )
        return {"result": True, "part": jsonBasicPart}
    else:
        return result
