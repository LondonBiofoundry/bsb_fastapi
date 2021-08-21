import base64
import basicsynbio as bsb
import os


def assemblytostring(assembly):
    bsb.export_sequences_to_file(assembly, "assembly.gb")
    with open("assembly.gb", "r") as f:
        output = f.read()
        f.close()
    os.remove("assembly.gb")
    return str(output)
