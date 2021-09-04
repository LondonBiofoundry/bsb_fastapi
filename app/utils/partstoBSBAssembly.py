from typing import List
import basicsynbio as bsb
from app.schema import basicPart

from app.utils.ItemtoPart import itemtopart


def partsToBSBAssembly(mybuild: List[basicPart]):
    """
    Converts frontend part objects into a basicsynbio assembly object
    """
    try:
        parts = []
        for item in mybuild:
            part = itemtopart(item)
            parts.append(part)
        parts.insert(0, "first_build")
        mytuple = tuple(parts)
        assembly = bsb.BasicAssembly(*mytuple)
        return assembly
    except Exception as e:
        return {"result": "failed", "detail": str(e)}
