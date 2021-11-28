from typing import Dict, List

from fastapi.datastructures import UploadFile
from app.schema import basicAssembly, basicPart
from app.utils.bsbPartsTobsbAssembly import bsbPartsTobsbAssembly
from app.utils.jsonPartToBsbPart import jsonPartToBsbPart

import basicsynbio as bsb


def validateAssembly(parts: List[basicPart], hashFileDictionary: Dict = None):
    try:
        if len(parts) == 0:
            return {"result": False, "message": "no parts within assembly"}
        else:
            bsbBasicParts = [
                jsonPartToBsbPart(part, hashFileDictionary) for part in parts
            ]
            for part in bsbBasicParts:
                if isinstance(part, str):
                    return {"result": False, "message": part}
            print("bsbBasicParts", bsbBasicParts)
            assembly = bsbPartsTobsbAssembly(bsbBasicParts, "validatedAssembly")
            if isinstance(assembly, bsb.BasicAssembly):
                return {"result": True}
            return {"result": False, "message": assembly}
    except Exception as e:
        return {"result": False, "message": str(e)}
