import base64
import basicsynbio as bsb
import os
from Bio import SeqIO
from app.schema import fileType, fileTypeData
import tempfile


def partToString(mypart, type: fileType = fileType.genbank):
    mypart.annotations["molecule_type"] = "DNA"
    suffix = fileTypeData[type].value["extension"]
    with tempfile.NamedTemporaryFile(suffix=suffix) as tmp:
        SeqIO.write(mypart, tmp.name, type)
        output = tmp.read()
    tmp.close()
    output_text = output.decode("utf-8")
    return output_text

