from fastapi.responses import FileResponse
from fastapi import FastAPI, Response
import tempfile
import io
import os
from typing import Callable
import basicsynbio as bsb
from pathlib import Path


def read_return_delete(file: str, media_type, filename):
    return_data = io.BytesIO()
    with open(file, "rb") as fo:
        return_data.write(fo.read())
    return_data.seek(0)

    resp = Response(
        return_data.getvalue(),
        media_type=media_type,
        headers={"Content-Disposition": f"attachment;filename={filename}"},
    )

    # os.remove(file)

    return resp


def create_file_execute_build_command_return(
    command: Callable, build, media_type: str, output_filename: str
):
    return_data = io.BytesIO()
    suffix = Path(output_filename).suffix
    with tempfile.NamedTemporaryFile(suffix=suffix) as tmp:
        command(build, tmp.name)
        return_data.write(tmp.read())
    return_data.seek(0)
    tmp.close()
    resp = Response(
        return_data.getvalue(),
        media_type=media_type,
        headers={"Content-Disposition": f"attachment;filename={output_filename}"},
    )
    return resp
