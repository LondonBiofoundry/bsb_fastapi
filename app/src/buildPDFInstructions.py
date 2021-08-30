from typing import List
from app.schema import basicBuild
from app.utils.returnBasicBuild import return_build
from app.utils.readReturnDelete import read_return_delete

import basicsynbio as bsb


def buildPDFInstructions(myBuild: List[basicBuild]):
    build = return_build(myBuild)
    filepath = bsb.pdf_instructions(build)
    return read_return_delete(filepath, "application/pdf", filepath)
