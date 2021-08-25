from typing import List
from app.schema import basicBuild
from app.utils.returnBasicBuild import return_build
from fastapi.responses import FileResponse

from app.utils.readReturnDelete import read_return_delete


def buildCSVs(myBuild: List[basicBuild]):
    build = return_build(myBuild)
    filepath = build.export_csvs()
    return read_return_delete(filepath, "application/zip", "archive.zip")
