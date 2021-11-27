from typing import Dict, List
from app.schema import basicAssembly
from app.utils.returnbasicAssembly import return_build
from fastapi.responses import FileResponse
from fastapi import HTTPException

from app.utils.readReturnDelete import read_return_delete


def buildCSVs(BuildArray: List[basicAssembly], hashFileDict: Dict = None):
    try:
        build = return_build(myBuild)
        filepath = build.export_csvs()
        return read_return_delete(filepath, "application/zip", "archive.zip")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
