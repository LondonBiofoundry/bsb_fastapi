from fastapi import UploadFile
import basicsynbio as bsb
from Bio import SeqIO
from io import StringIO
from typing import List
from app.schema import fileType

from app.utils.partToString import partToString


def returnBasicPartFromUploadFileInitial(
    file: UploadFile, type: fileType, addiseq: bool
) -> bsb.BasicPart:
    try:
        if type == fileType.SBOL:
            basic_part = bsb.import_sbol_part(file.file, addiseq)
        else:
            seqrec = SeqIO.read(StringIO(str(file.file.read(), 'utf-8')),type)
            return bsb.seqrec2part(seqrec, addiseq)
        return basic_part
    except Exception as e:
            return {"error": str(e)}


def basicPartsFromUploadFile(
    file: UploadFile, type: fileType, addiseq: bool
) -> List[bsb.BasicPart]:
    try:
        if type == fileType.SBOL:
            return {"error": "SBOL file type cannot contain multiple parts"}
        else:
            seqrecs = SeqIO.parse(StringIO(str(file.file.read(), 'utf-8')),type)
            basic_parts = yield from (bsb.seqrec2part(seqrec, addiseq) for seqrec in seqrecs)
            parts_array = [
                {
                    "label": part.id,
                    "seq": str(part.seq),
                    "binaryString": partToString(part, type),
                }
                for part in basic_parts
            ]
            return {"result": "success", "partsarray": parts_array}
    except Exception as e:
            return {"error": str(e)}

