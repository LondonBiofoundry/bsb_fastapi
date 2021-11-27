from fastapi import File, UploadFile
import basicsynbio as bsb
from app.schema import basicPartType, fileType, fileTypeData

from app.utils.basicPartFromFile import returnBasicPartsFromUploadFileInitial
from app.utils.bsbBasicPartToJsonbasicPart import bsbBasicPartToJsonbasicPart


async def fileUploadMultiple(
    type: fileType, addiseq: bool, file: UploadFile = File(...)
):
    try:
        bsbBasicParts = returnBasicPartsFromUploadFileInitial(file, type, addiseq)
        if isinstance(bsbBasicParts, str):
            return {
                "result": False,
                "message": bsbBasicParts,
            }
        for bsbBasicPart in bsbBasicParts:
            if not isinstance(bsbBasicPart, bsb.BasicPart):
                return {
                    "result": False,
                    "message": "Unable to convert record into BasicSynBio part ${bsbBasicPart}",
                }
        print("Just before turning to json basic parts")
        jsonBasicParts = [
            bsbBasicPartToJsonbasicPart(
                bsbBasicPart, basicPartType.uploadMultiple, file, index
            )
            for index, bsbBasicPart in enumerate(bsbBasicParts)
        ]
        return {"result": True, "parts": jsonBasicParts}
    except Exception as e:
        raise e
        # return {"result": False, "message": }
