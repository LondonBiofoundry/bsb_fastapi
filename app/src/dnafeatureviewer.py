import basicsynbio as bsb
from app.utils.ItemtoPart import itemtopart
from dna_features_viewer import BiopythonTranslator
import base64
import matplotlib
import os

matplotlib.use("Agg")


def dnafeaturesviewerpng(BSBpart):
    try:
        bsbpart = itemtopart(BSBpart)
        bsb.export_sequences_to_file(bsbpart, "intermediate.gb")
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

        return {"success": True, "base64image": returnstr}
    except Exception as e:
        return {"error2": str(e)}
