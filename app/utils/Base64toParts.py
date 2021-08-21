import base64
import basicsynbio as bsb
import os
from Bio import SeqIO


def base64toparts(base64string, filename, assemblyType, addiseq):
    decodedb64 = base64.b64decode(base64string)
    decodedbinary = decodedb64.decode("utf-8")
    mylist = decodedbinary.strip("][").replace("'", "").split(", ")
    smallerlist = mylist[0]
    myarray = smallerlist.split(",")
    myarray_int = map(int, myarray)
    res = "".join(map(chr, myarray_int))
    f = open(filename, "w+")
    f.write(res)
    f.close()
    if assemblyType == "fasta":
        basic_parts = bsb.import_parts(filename, "fasta", addiseq)
        parts_array = [
            {
                "label": part.id,
                "seq": str(part.seq),
                "binaryString": parttostring(part, assemblyType),
            }
            for part in basic_parts
        ]
    if assemblyType == "genbank":
        basic_parts = bsb.import_parts(filename, "genbank", addiseq)
        parts_array = [
            {
                "label": part.id,
                "seq": str(part.seq),
                "binaryString": parttostring(part, assemblyType),
            }
            for part in basic_parts
        ]
    return filename, parts_array


def parttostring(mypart, assemblyType):
    mypart.annotations["molecule_type"] = "DNA"
    if assemblyType == "genbank":
        SeqIO.write(mypart, "mypart.gb", "genbank")
        with open("mypart.gb", "r") as f:
            output = f.read()
            f.close()
        os.remove("mypart.gb")
    if assemblyType == "fasta":
        SeqIO.write(mypart, "mypart.fasta", "fasta")
        with open("mypart.gb", "r") as f:
            output = f.read()
            f.close()
        os.remove("mypart.gb")
    return str(output)
