from fastapi import File, UploadFile
import basicsynbio as bsb
from typing import List
from pathlib import Path
import os
from tempfile import NamedTemporaryFile
import shutil
from app.schema import fileType, fileTypeData

from app.utils.partToString import partToString


def get_file_path_name(file: UploadFile) -> Path:
    return Path(os.path.join(Path.cwd(), Path(file.filename)))


def create_temp_file(upload_file: UploadFile) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
    finally:
        upload_file.file.close()
    return tmp


def returnBasicPartFromUploadFile(
    file: UploadFile, type: fileType, addiseq: bool
) -> bsb.BasicPart:
    try:
        tmp = create_temp_file(file)
        if type == fileType.SBOL:
            basic_part = bsb.import_sbol_part(tmp.name, addiseq)
        else:
            basic_part = bsb.import_part(tmp.name, type, addiseq)
        tmp.close()
        return basic_part
    except Exception as e:
        try:
            tmp.close()
        finally:
            return {"error": str(e)}


def basicPartsFromUploadFile(
    file: UploadFile, type: fileType, addiseq: bool
) -> List[bsb.BasicPart]:
    try:
        if type == fileType.SBOL:
            return {"error": "SBOL file type cannot contain multiple parts"}
        else:
            tmp = create_temp_file(file)
            basic_parts = bsb.import_parts(tmp.name, type, addiseq)
            parts_array = [
                {
                    "label": part.id,
                    "seq": str(part.seq),
                    "binaryString": partToString(part, type),
                }
                for part in basic_parts
            ]
            tmp.close()
            return {"result": "success", "partsarray": parts_array}
    except Exception as e:
        try:
            tmp.close()
        finally:
            return {"error": str(e)}
