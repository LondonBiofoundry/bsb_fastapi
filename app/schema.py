from pydantic import BaseModel
from typing import Optional, List
from enum import Enum


class basicPart(BaseModel):
    id: str
    accessor: Optional[str] = None
    binaryString: Optional[str] = None
    base64: Optional[str] = None
    collection: Optional[str] = None
    description: Optional[str] = None
    label: Optional[str] = None
    multiple: Optional[bool] = None
    index: Optional[int] = None
    type: Optional[str] = None


class basicBuild(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    parts: Optional[List[basicPart]] = None

class fileTypeInformation():
    name: str
    extension: str

class fileTypeData(fileTypeInformation,Enum):
    genbank = {"name":"genbank","extension":".gb"}
    fasta = {"name":"fasta","extension":".fasta"}
    SBOL = {"name":"SBOL","extension":".rdf"}

class fileType(str, Enum):
    genbank = "genbank"
    fasta = "fasta"
    SBOL = "SBOL"

class fileUploadArgs(BaseModel):
    addiseq: bool
    type: fileType
