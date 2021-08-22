from fastapi import File, UploadFile
import basicsynbio as bsb
from pathlib import Path
import os
from app.schema import fileType, fileTypeData

from app.utils.fileHandlers import save_upload_file

def get_file_path_name(file: UploadFile) -> Path:
    return Path(os.path.join(Path.cwd(),Path(file.filename)))


def returnBasicPartFromUploadFile(file: UploadFile, type: fileType, addiseq: bool) -> bsb.BasicPart:
    try:
        filepath = get_file_path_name(file)
        save_upload_file(file,filepath)
        if type == fileType.SBOL:
            basic_part = bsb.import_sbol_part(filepath, addiseq)
        else:
            basic_part = bsb.import_part(filepath, type, addiseq)
        os.remove(filepath)
        return basic_part
    except Exception as e:
        return {"error": str(e)}