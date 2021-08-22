from typing import List
from app.schema import basicBuild
from app.utils.returnBasicBuild import return_build

def buildCSVs(myBuild: List[basicBuild]):
    build = return_build(myBuild)
    print(build)
    return {"data": "true"}