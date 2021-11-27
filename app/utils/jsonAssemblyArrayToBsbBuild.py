import basicsynbio as bsb
from typing import Dict, List, Union

from app.schema import basicAssembly
from app.utils.bsbPartsTobsbAssembly import bsbPartsTobsbAssembly
from app.utils.jsonPartToBsbPart import jsonPartToBsbPart


def jsonAssemblyArrayToBsbBuild(
    assemblyArray: List[basicAssembly], hashFileDict: Dict = None
) -> Union[bsb.BasicBuild, str]:
    try:
        bsbAssemblies = []
        for assembly in assemblyArray:
            bsbParts = []
            for jsonPart in assembly["parts"]:
                bsbPart = jsonPartToBsbPart(jsonPart, hashFileDict)
                if isinstance(bsbPart, str):
                    return bsbPart
                bsbParts.append(bsbPart)
            assemblyId = "Basic Assembly"
            if assembly["id"]:
                assemblyId = assembly["id"]
            if assembly["name"]:
                assemblyId = assembly["id"]
            bsbAssembly = bsbPartsTobsbAssembly(bsbParts, assemblyId)
            if isinstance(bsbAssembly, str):
                return bsbPart
        bsbBuild = bsb.BasicBuild(*bsbAssemblies)
        return bsbBuild
    except Exception as e:
        return str(e)

    return True
