import base64
import basicsynbio as bsb
import os


def itemtopart(item):
    if item["collection"] == "BASIC_CDS_PARTS":
        return bsb.BASIC_CDS_PARTS["v0.1"][item["accessor"]]
    if item["collection"] == "BASIC_SEVA_PARTS":
        return bsb.BASIC_SEVA_PARTS["v0.1"][item["accessor"]]
    if item["collection"] == "BASIC_BIOLEGIO_LINKERS":
        return bsb.BASIC_BIOLEGIO_LINKERS["v0.1"][item["accessor"]]
    if item["collection"] == "BASIC_PROMOTER_PARTS":
        return bsb.BASIC_PROMOTER_PARTS["v0.1"][item["accessor"]]
    else:
        if item["type"] == "genbank":
            if item["multiple"]:
                mypart, myfilename = base64partstopart(
                    item["base64"], "hello.gb", "genbank", item["index"]
                )
            else:
                mypart, myfilename = base64topart(item["base64"], "hello.gb")
        if item["type"] == "fasta":
            if item["multiple"]:
                mypart, myfilename = base64partstopart(
                    item["base64"], "hello.fasta", "fasta", item["index"]
                )
            else:
                mypart, myfilename = base64topart(item["base64"], "hello.fasta")
        if item["type"] == "SBOL":
            mypart, myfilename = base64topart(item["base64"], "hello.rdf")
        os.remove(myfilename)
        return mypart


def base64topart(base64string, filename):
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
    part = bsb.import_part(filename, "genbank")
    return part, filename


def base64partstopart(base64string, filename, assemblyType, index):
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
        basic_parts = bsb.import_parts(filename, "fasta")
        parts_array = [part for part in basic_parts]
    if assemblyType == "genbank":
        basic_parts = bsb.import_parts(filename, "genbank")
        parts_array = [part for part in basic_parts]
    mypart = parts_array[index]
    return mypart, filename
