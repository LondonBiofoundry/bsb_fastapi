from typing import List
from app.schema import basicAssembly
from app.utils.returnbasicAssembly import return_build
from fastapi.responses import FileResponse
from fastapi import HTTPException
import json

from app.utils.readReturnDelete import create_file_execute_build_command_return

import basicsynbio as bsb


def buildUniqueAssemblies(myBuild: List[basicAssembly]):
    try:
        build = return_build(myBuild)
        unique_assemblies = (assembly for assembly in build.basic_assemblies)
        return create_file_execute_build_command_return(
            bsb.export_sequences_to_file,
            unique_assemblies,
            "chemical/seq-na-genbank",
            "Unique_Assemblies.gb",
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
