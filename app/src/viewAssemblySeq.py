from typing import Dict, List

from fastapi.datastructures import UploadFile
from app.schema import basicAssembly, basicPart
from app.utils.bsbPartsTobsbAssembly import bsbPartsTobsbAssembly
from app.utils.jsonPartToBsbPart import jsonPartToBsbPart

import basicsynbio as bsb


def return_assembly_sequence(
    Qualifier: str, parts: List[basicPart], hashFileDictionary: Dict = None
):
    def extract_feature(myfeature):
        try:
            # myfeature.qualifiers[Qualifier][0]:
            name = myfeature.qualifiers[Qualifier][0]
            try:
                last_location = myfeature.location.parts[0]
                return {
                    "start": last_location.start,
                    "end": last_location.end,
                    "name": name,
                    "direction": last_location.strand,
                }
            except:
                return {
                    "start": myfeature.location.start,
                    "end": myfeature.location.end,
                    "name": name,
                    "direction": myfeature.strand,
                }
        except:
            return

    try:

        if len(parts) == 0:
            return {"result": False, "message": "no parts within assembly"}
        else:
            bsbBasicParts = [
                jsonPartToBsbPart(part, hashFileDictionary) for part in parts
            ]
            for part in bsbBasicParts:
                if isinstance(part, str):
                    return {"result": False, "message": part}
            assembly = bsbPartsTobsbAssembly(bsbBasicParts, "validatedAssembly")
            if isinstance(assembly, bsb.BasicAssembly):
                part = assembly.return_part(name="new-part")
                print("generated-part", part)
                print("generated-part", part.seq)
                print("generated-part", part.id)
                annotations = map(extract_feature, part.features)
                return {
                    "result": True,
                    "message": {"seq": str(part.seq), "annotations": list(annotations)},
                }
            return {"result": False, "message": assembly}
    except Exception as e:
        print(e)
        return {"result": False, "message": str(e)}
