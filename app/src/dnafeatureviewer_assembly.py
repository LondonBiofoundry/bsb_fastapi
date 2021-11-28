from typing import Dict, List
import basicsynbio as bsb
from app.schema import basicPart
from app.utils.ItemtoPart import itemtopart
from dna_features_viewer import BiopythonTranslator
import base64
import matplotlib
import os
from app.utils.bsbPartsTobsbAssembly import bsbPartsTobsbAssembly
from app.utils.jsonPartToBsbPart import jsonPartToBsbPart

from app.utils.partstoBSBAssembly import partsToBSBAssembly

matplotlib.use("Agg")


def dnafeaturesviewerpng_assembly(
    parts: List[basicPart], hashFileDictionary: Dict = None
):
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
            print("bsbBasicParts", bsbBasicParts)
            assembly = bsbPartsTobsbAssembly(bsbBasicParts, "validatedAssembly")
            if isinstance(assembly, bsb.BasicAssembly):
                bsb.export_sequences_to_file(assembly, "intermediate.gb")
                graphic_record = BiopythonTranslator().translate_record(
                    "intermediate.gb"
                )
                ax, _ = graphic_record.plot(
                    figure_width=10, strand_in_label_threshold=7
                )
                ax.figure.tight_layout()
                ax.figure.savefig("intermediate.png")
                with open("intermediate.png", "rb") as img_file:
                    imageb64string = base64.b64encode(img_file.read())
                img_file.close()
                returnstr = imageb64string.decode("utf-8")
                os.remove("intermediate.gb")
                os.remove("intermediate.png")

                return {"success": True, "base64image": returnstr}
            return {"result": False, "message": assembly}
    except Exception as e:
        return {"result": False, "message": str(e)}
