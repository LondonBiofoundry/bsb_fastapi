from typing import List
from app.schema import basicAssembly, basicPart
from app.utils.returnbasicAssembly import return_build
from fastapi.responses import FileResponse
from fastapi import HTTPException

from app.utils.ItemtoPart import itemtopart
from app.utils.partstoBSBAssembly import partsToBSBAssembly

from app.src.viewpartlabels import get_qualifiers

import basicsynbio as bsb


def viewseqlabels(mybuild: List[basicPart]):
    try:
        if len(mybuild) == 0:
            return {"result": "no parts within assembly"}
        else:
            assembly = partsToBSBAssembly(mybuild)
            if isinstance(assembly, bsb.BasicAssembly):
                part_from_build = assembly.return_part()
                options = list(set(map(get_qualifiers, part_from_build.features)))
                options.append("Feature")
                return options
            return assembly
    except Exception as e:
        return {"result": "failed", "detail": str(e)}
