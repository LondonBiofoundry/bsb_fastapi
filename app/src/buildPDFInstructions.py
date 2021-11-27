from typing import Dict, List
from app.schema import basicAssembly
from app.utils.jsonAssemblyArrayToBsbBuild import jsonAssemblyArrayToBsbBuild

# from app.utils.returnbasicAssembly import return_build
from app.utils.readReturnDelete import read_return_delete

import basicsynbio as bsb


def buildPDFInstructions(assemblyArray: List[basicAssembly], hashFileDict: Dict = None):
    try:
        bsbBuild = jsonAssemblyArrayToBsbBuild(assemblyArray, hashFileDict)
        if isinstance(bsbBuild, str):
            return {"result": False, "message": bsbBuild}
        filepath = bsb.pdf_instructions(bsbBuild)
        return read_return_delete(filepath, "application/pdf", filepath)
    except Exception as e:
        return {"result": False, "message": str(e)}
