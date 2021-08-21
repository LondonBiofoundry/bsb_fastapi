import base64
import basicsynbio as bsb
import os
from Bio import SeqIO


def partToString(mypart):
    mypart.annotations["molecule_type"] = "DNA"
    SeqIO.write(mypart, "mypart.gb", "genbank")
    with open("mypart.gb", "r") as f:
        output = f.read()
        f.close()
    os.remove("mypart.gb")
    return str(output)
