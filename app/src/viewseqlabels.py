from typing import Dict, List
from app.schema import basicAssembly, basicPart

from fastapi.responses import FileResponse
from fastapi import HTTPException

from app.utils.ItemtoPart import itemtopart
from app.utils.bsbPartsTobsbAssembly import bsbPartsTobsbAssembly
from app.utils.jsonPartToBsbPart import jsonPartToBsbPart
from app.utils.partstoBSBAssembly import partsToBSBAssembly

from app.src.viewpartlabels import get_qualifiers

import basicsynbio as bsb


def viewseqlabels(parts: List[basicPart], hashFileDictionary: Dict = None):
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
                part_from_build = assembly.return_part()
                options = list(set(map(get_qualifiers, part_from_build.features)))
                options.append("Feature")
                return options
            return {"result": False, "message": assembly}
    except Exception as e:
        return {"result": False, "message": str(e)}
