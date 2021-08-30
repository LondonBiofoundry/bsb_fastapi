from typing import List
from app.schema import basicBuild, basicPart
from app.utils.returnBasicBuild import return_build
from fastapi.responses import FileResponse
from fastapi import HTTPException

from app.utils.readReturnDelete import read_return_delete
from app.utils.ItemtoPart import itemtopart

import basicsynbio as bsb


def validateAssembly(mybuild: List[basicPart]):
    try:
        if len(mybuild) == 0:
            return {"result": "no parts within assembly"}
        else:
            parts = []
            for item in mybuild:
                part = itemtopart(item)
                parts.append(part)
            parts.insert(0, "first_build")
            mytuple = tuple(parts)
            assembly = bsb.BasicAssembly(*mytuple)
            return {"result": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
