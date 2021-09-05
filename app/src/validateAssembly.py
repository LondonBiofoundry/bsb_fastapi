from typing import List
from app.schema import basicBuild, basicPart
from app.utils.returnBasicBuild import return_build
from fastapi.responses import FileResponse
from fastapi import HTTPException

from app.utils.ItemtoPart import itemtopart
from app.utils.partstoBSBAssembly import partsToBSBAssembly

import basicsynbio as bsb


def validateAssembly(mybuild: List[basicPart]):
    try:
        if len(mybuild) == 0:
            return {"result": "no parts within assembly"}
        else:
            assembly = partsToBSBAssembly(mybuild)
            if isinstance(assembly, bsb.BasicAssembly):
                return {"result": "success"}
            return assembly
    except Exception as e:
        return {"result": "failed", "detail": str(e)}
