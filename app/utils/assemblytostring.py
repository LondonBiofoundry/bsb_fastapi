import base64
import basicsynbio as bsb
from app.schema import fileType, fileTypeData
import tempfile
import os


def assemblytostring(assembly):
    suffix = fileTypeData[type].value["extension"]
    with tempfile.NamedTemporaryFile(suffix=suffix) as tmp:
        bsb.export_sequences_to_file(assembly, tmp.name)
        output = tmp.read()
    tmp.close()
    output_text = output.decode("utf-8")
    return output_text
