from flask import send_file
import io
import os


def read_return_delete(file, file_type, file_name):
    return_data = io.BytesIO()
    with open(file, "rb") as fo:
        return_data.write(fo.read())
    return_data.seek(0)
    os.remove(file)
    return send_file(
        return_data,
        mimetype=file_type,
        attachment_filename=file_name,
        as_attachment=True,
    )
