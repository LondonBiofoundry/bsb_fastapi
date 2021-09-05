from fastapi import File, UploadFile
import basicsynbio as bsb
from typing import List
from pathlib import Path
import os
from app.schema import fileType, fileTypeData

from app.utils.fileHandlers import save_upload_file
from app.utils.partToString import partToString


def get_file_path_name(file: UploadFile) -> Path:
    return Path(os.path.join(Path.cwd(), Path(file.filename)))


def returnBasicPartFromUploadFile(
    file: UploadFile, type: fileType, addiseq: bool
) -> bsb.BasicPart:
    try:
        filepath = get_file_path_name(file)
        save_upload_file(file, filepath)
        if type == fileType.SBOL:
            basic_part = bsb.import_sbol_part(filepath, addiseq)
        else:
            basic_part = bsb.import_part(filepath, type, addiseq)
        os.remove(filepath)
        return basic_part
    except Exception as e:
        try:
            filepath = get_file_path_name(file)
            os.remove(filepath)
        finally:
            return {"error": str(e)}


def basicPartsFromUploadFile(
    file: UploadFile, type: fileType, addiseq: bool
) -> List[bsb.BasicPart]:
    try:
        if type == fileType.SBOL:
            return {"error": "SBOL file type cannot contain multiple parts"}
        else:
            filepath = get_file_path_name(file)
            save_upload_file(file, filepath)
            basic_parts = bsb.import_parts(filepath, type, addiseq)
            parts_array = [
                {
                    "label": part.id,
                    "seq": str(part.seq),
                    "binaryString": partToString(part, type),
                }
                for part in basic_parts
            ]
            os.remove(filepath)
            return {"result": "success", "partsarray": parts_array}
    except Exception as e:
        try:
            filepath = get_file_path_name(file)
            os.remove(filepath)
        finally:
            return {"error": str(e)}
