from typing import List
from app.schema import basicAssembly
from app.utils.returnbasicAssembly import return_build
from fastapi.responses import FileResponse
from fastapi import HTTPException
import json

from app.utils.readReturnDelete import create_file_execute_build_command_return

import basicsynbio as bsb


def buildUniqueParts(myBuild: List[basicAssembly]):
    build = return_build(myBuild)
    return create_file_execute_build_command_return(
        bsb.export_sequences_to_file,
        build.unique_parts,
        "chemical/seq-na-genbank",
        "Unique_Parts.gb",
    )
