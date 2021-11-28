from typing import Dict, List
from app.schema import basicAssembly

from fastapi.responses import FileResponse
from fastapi import HTTPException
import json
from app.utils.jsonAssemblyArrayToBsbBuild import jsonAssemblyArrayToBsbBuild

from app.utils.readReturnDelete import create_file_execute_build_command_return

import basicsynbio as bsb


def buildUniqueParts(assemblyArray: List[basicAssembly], hashFileDict: Dict = None):
    try:
        bsbBuild = jsonAssemblyArrayToBsbBuild(assemblyArray, hashFileDict)
        if isinstance(bsbBuild, str):
            return {"result": False, "message": bsbBuild}
        return create_file_execute_build_command_return(
            bsb.export_sequences_to_file,
            bsbBuild.unique_parts,
            "chemical/seq-na-genbank",
            "Unique_Parts.gb",
        )
    except Exception as e:
        return {"result": False, "message": bsbBuild}
