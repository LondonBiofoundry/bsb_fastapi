import base64
import basicsynbio as bsb
import os
from Bio import SeqIO


def partToString(mypart):
    mypart.annotations["molecule_type"] = "DNA"
    SeqIO.write(mypart, "mypart.gb", "genbank")
    text_file = open("mypart.gb", "r")
    data = text_file.read()
    text_file.close()
    os.remove("mypart.gb")
    return str(data)
