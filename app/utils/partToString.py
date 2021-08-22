import base64
import basicsynbio as bsb
import os
from Bio import SeqIO
from app.schema import fileType, fileTypeData


def createPathForType(type: fileType = fileType.genbank):
    return "mypart" + fileTypeData[type].extension


def partToString(mypart, type: fileType = fileType.genbank):
    filename = createPathForType(type)
    mypart.annotations["molecule_type"] = "DNA"
    SeqIO.write(mypart, filename, type)
    with open(filename, "r") as f:
        output = f.read()
        f.close()
    os.remove(filename)
    return str(output)
