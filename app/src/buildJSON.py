from typing import List
from app.schema import basicAssembly
from app.utils.returnbasicAssembly import return_build
from fastapi.responses import FileResponse
from fastapi import HTTPException
import json

from app.utils.readReturnDelete import read_return_delete

import basicsynbio as bsb


def buildJSON(myBuild: List[basicAssembly]):
    try:
        build = return_build(myBuild)
        with open("my_build.json", "w") as json_file:
            json.dump(build, json_file, cls=bsb.BuildEncoder, indent=4)
        return read_return_delete("my_build.json", "application/json", "my_build.json")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
