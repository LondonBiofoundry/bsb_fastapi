from typing import Dict
import basicsynbio as bsb
from app.schema import basicPart
from dna_features_viewer import BiopythonTranslator
import base64
import matplotlib
import os

from app.utils.jsonPartToBsbPart import jsonPartToBsbPart

matplotlib.use("Agg")


def dnafeaturesviewerpng(part: basicPart, hashFileDictionary: Dict = None):
    try:
        bsbPart = jsonPartToBsbPart(part, hashFileDictionary)
        bsb.export_sequences_to_file(bsbPart, "intermediate.gb")
        graphic_record = BiopythonTranslator().translate_record("intermediate.gb")
        ax, _ = graphic_record.plot(figure_width=10, strand_in_label_threshold=7)
        ax.figure.tight_layout()
        ax.figure.savefig("intermediate.png")
        with open("intermediate.png", "rb") as img_file:
            imageb64string = base64.b64encode(img_file.read())
        img_file.close()
        returnstr = imageb64string.decode("utf-8")
        os.remove("intermediate.gb")
        os.remove("intermediate.png")

        return {"result": True, "base64image": returnstr}
    except Exception as e:
        return {"result": False, "message": str(e)}
