import hashlib
from typing import List

from fastapi import UploadFile


def createHashFileDictionary(files: List[UploadFile]):
    hashFileDictionary = {}
    for file in files:
        hash = getHashFromFile(file)
        updateDict = dict({hash: file})
        hashFileDictionary.update(updateDict)
    return hashFileDictionary


def getHashFromFile(file: UploadFile):
    file.file.seek(0)
    return hashlib.md5(file.file.read()).hexdigest()
