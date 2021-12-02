from typing import Dict, List
from app.schema import basicAssembly
import basicsynbio as bsb

from app.utils.jsonAssemblyArrayToBsbBuild import jsonAssemblyArrayToBsbBuild

from app.utils.readReturnDelete import read_return_delete, returnFileResponse


def buildCSVs(
    background_tasks, assemblyArray: List[basicAssembly], hashFileDict: Dict = None
):
    try:
        bsbBuild = jsonAssemblyArrayToBsbBuild(assemblyArray, hashFileDict)
        if isinstance(bsbBuild, str):
            return {"result": False, "message": bsbBuild}
        filepath = bsb.cam.export_csvs(bsbBuild)
        return returnFileResponse(
            filepath, "application/zip", "archive.zip", background_tasks
        )
    except Exception as e:
        return {"result": False, "message": str(e)}
