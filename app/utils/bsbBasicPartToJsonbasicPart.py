import basicsynbio as bsb
import hashlib
from fastapi.datastructures import UploadFile

from app.schema import basicPart, basicPartType


def bsbBasicPartToJsonbasicPart(
    bsbBasicPart: bsb.BasicPart,
    uploadType: basicPartType,
    file: UploadFile = None,
    index: int = None,
) -> basicPart:
    jsonDocument = {
        # A unique identifier for the part
        "id": bsbBasicPart.id,
        # A human readable name (non unique): of the part
        "label": bsbBasicPart.name,
        # The type of bsb part
        "type": uploadType,
        # A description of the part
        "description": bsbBasicPart.description,
        # The sequence of the available part
        "seq": str(bsbBasicPart.seq),
        # The sequence of the available part
    }
    if not file == None:
        # Add the fileId attribute of the jsonBasicPart
        file.file.seek(0)
        jsonDocument["fileId"] = hashlib.md5(file.file.read()).hexdigest()
    if not index == None:
        # Add the index attribute of the jsonBasicPart
        jsonDocument["index"] = index
    return jsonDocument
