from typing import Dict, List
from app.schema import basicAssembly

from fastapi.responses import FileResponse
from fastapi import HTTPException
import json
from app.utils.jsonAssemblyArrayToBsbBuild import jsonAssemblyArrayToBsbBuild

from app.utils.readReturnDelete import read_return_delete

import basicsynbio as bsb


def buildJSON(assemblyArray: List[basicAssembly], hashFileDict: Dict = None):
    try:
        bsbBuild = jsonAssemblyArrayToBsbBuild(assemblyArray, hashFileDict)
        if isinstance(bsbBuild, str):
            return {"result": False, "message": bsbBuild}
        with open("my_build.json", "w") as json_file:
            json.dump(bsbBuild, json_file, cls=bsb.BuildEncoder, indent=4)
        return read_return_delete("my_build.json", "application/json", "my_build.json")
    except Exception as e:
        return {"result": False, "message": bsbBuild}
