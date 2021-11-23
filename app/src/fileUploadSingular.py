from fastapi import File, UploadFile
import basicsynbio as bsb
from app.schema import fileType, fileTypeData

from app.utils.basicPartFromFile import returnBasicPartFromUploadFile




def fileUploadSingular(
    type: fileType, addiseq: bool, file: UploadFile = File(...)
):
    result = returnBasicPartFromUploadFile(file, type, addiseq)
    if isinstance(result, bsb.BasicPart):
        return {"result": "success", "seq": str(result.seq)}
    else:
        return result
