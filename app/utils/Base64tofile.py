import base64
import basicsynbio as bsb


def base64tofile(base64string, filename, assemblyType, addiseq):
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
    if assemblyType == "SBOL":
        basic_part = bsb.import_sbol_part(filename, addiseq)
    if assemblyType == "fasta":
        basic_part = bsb.import_part(filename, "fasta", addiseq)
    if assemblyType == "genbank":
        basic_part = bsb.import_part(filename, "genbank", addiseq)
    sequence = str(basic_part.seq)
    return filename, sequence
