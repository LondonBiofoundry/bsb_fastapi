from typing import List
from app.schema import basicAssembly
from app.utils.returnbasicAssembly import return_build
from app.utils.readReturnDelete import read_return_delete

import basicsynbio as bsb


def buildPDFInstructions(myBuild: List[basicAssembly]):
    build = return_build(myBuild)
    filepath = bsb.pdf_instructions(build)
    return read_return_delete(filepath, "application/pdf", filepath)
