from typing import List
from app.schema import basicBuild
from app.utils.returnBasicBuild import return_build
from fastapi.responses import FileResponse
from fastapi import HTTPException
import json

from app.utils.readReturnDelete import read_return_delete

import basicsynbio as bsb


def buildUniqueAssemblies(myBuild: List[basicBuild]):
    try:
        build = return_build(myBuild)
        unique_assemblies = (assembly for assembly in build.basic_assemblies)
        bsb.export_sequences_to_file(unique_assemblies, "Unique_Assemblies.gb")
        return read_return_delete(
            "Unique_Assemblies.gb", "chemical/seq-na-genbank", "Unique_Assemblies.gb"
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
