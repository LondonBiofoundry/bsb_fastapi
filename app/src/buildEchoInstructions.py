from typing import List
from app.schema import basicAssembly

# from app.utils.returnbasicAssembly import return_build
from app.utils.readReturnDelete import create_file_execute_build_command_return

import basicsynbio as bsb


def buildEchoInstructions(myBuild: List[basicAssembly]):
    # build = return_build(myBuild)
    return create_file_execute_build_command_return(
        bsb.export_echo_assembly, build, "application/zip", "archive.zip"
    )
