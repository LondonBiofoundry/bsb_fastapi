from typing import List, Union
import basicsynbio as bsb

from app.utils.ItemtoPart import itemtopart


def bsbPartsTobsbAssembly(
    bsbParts: List[bsb.BasicPart], assemblyId: str
) -> Union[bsb.BasicAssembly, str]:
    """
    Converts frontend part objects into a basicsynbio assembly object
    """
    try:
        parts = []
        for bsbPart in bsbParts:
            parts.append(bsbPart)
        parts.insert(0, assemblyId)
        mytuple = tuple(parts)
        assembly = bsb.BasicAssembly(*mytuple)
        return assembly
    except Exception as e:
        return str(e)
