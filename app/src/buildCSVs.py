from typing import Dict, List
from app.schema import basicAssembly
import basicsynbio as bsb

from app.utils.jsonAssemblyArrayToBsbBuild import jsonAssemblyArrayToBsbBuild

from app.utils.readReturnDelete import read_return_delete


def buildCSVs(assemblyArray: List[basicAssembly], hashFileDict: Dict = None):
    try:
        bsbBuild = jsonAssemblyArrayToBsbBuild(assemblyArray, hashFileDict)
        if isinstance(bsbBuild, str):
            return {"result": False, "message": bsbBuild}
        filepath = bsb.cam.export_csvs(bsbBuild)
        return read_return_delete(filepath, "application/zip", "archive.zip")
    except Exception as e:
        return {"result": False, "message": str(e)}
