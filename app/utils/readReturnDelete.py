from fastapi.responses import FileResponse
from fastapi import FastAPI, Response
import io
import os


def read_return_delete(file, media_type, filename):
    return_data = io.BytesIO()
    with open(file, "rb") as fo:
        return_data.write(fo.read())
    return_data.seek(0)

    resp = Response(return_data.getvalue(), media_type="application/x-zip-compressed", headers={
        'Content-Disposition': f'attachment;filename={filename}'
    })

    os.remove(file)

    return resp
