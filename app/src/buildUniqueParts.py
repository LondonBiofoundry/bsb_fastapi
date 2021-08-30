from typing import List
from app.schema import basicBuild
from app.utils.returnBasicBuild import return_build
from fastapi.responses import FileResponse
from fastapi import HTTPException
import json

from app.utils.readReturnDelete import read_return_delete

import basicsynbio as bsb


def buildUniqueParts(myBuild: List[basicBuild]):
    try:
        build = return_build(myBuild)
        bsb.export_sequences_to_file(build.unique_parts, "Unique_Parts.gb")
        return read_return_delete(
            "Unique_Parts.gb", "Unique_Parts.gb", "Unique_Parts.gb"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
