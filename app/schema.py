from pydantic import BaseModel
from typing import Optional, List, Any
from enum import Enum
from fastapi import File, UploadFile
from app.schema_examples.exampleBasicAssembly import exampleBasicAssembly
from app.schema_examples.exampleBasicPart import exampleBasicPart


class basicPartType(str, Enum):
    uploadSingle = "uploadSingle"
    uploadMultiple = "uploadMultiple"
    collection = "collection"


class basicPart(BaseModel):
    # A unique identifier for the part
    id: str
    # A human readable name (non unique): of the part
    label: Optional[str] = None
    # The type of bsb part
    type: basicPartType
    # A description of the part
    description: Optional[str] = None
    # The sequence of the available part
    seq: Optional[str] = None
    # (If Collection): The key of the collection version
    accessor: Optional[str] = None
    # (If Collection): The bsb collection that the part comes from
    collection: Optional[str] = None
    # (If Collection): The version of the basicsynbio collection that the part comes from
    version: Optional[str] = None
    # (If upload) hash of the uploaded file used to recognize associated files
    fileId: Optional[str] = None
    # (If upload) addiseq, wether or not the uploaded file was parsed with addiseq argument
    addiseq: Optional[bool] = None
    # (If multipleUpload): The index of the individual part
    index: Optional[int] = None

    class Config:
        schema_extra = {"example": exampleBasicPart}


class basicAssembly(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    parts: Optional[List[basicPart]] = None

    class Config:
        schema_extra = {"example": exampleBasicAssembly}


class fileTypeInformation:
    name: str
    extension: str


class fileTypeData(fileTypeInformation, Enum):
    genbank = {"name": "genbank", "extension": ".gb"}
    fasta = {"name": "fasta", "extension": ".fasta"}
    SBOL = {"name": "SBOL", "extension": ".rdf"}


class fileType(str, Enum):
    genbank = "genbank"
    fasta = "fasta"
    SBOL = "SBOL"


class fileUploadArgs(BaseModel):
    addiseq: bool
    type: fileType


class collectionVersionInstance(BaseModel):
    name: str
    parts: List[basicPart]


class collection(BaseModel):
    name: str
    availableVersions: List[str]
    versions: List[collectionVersionInstance]


class responseCollectionsData(BaseModel):
    data: List[collection]


class responseCollectionsName(BaseModel):
    data: List[str]


class responseSingularFileUpload(BaseModel):
    result: bool
    message: Optional[str] = None
    part: Optional[basicPart] = None


class responseMultipleFileUpload(BaseModel):
    result: bool
    message: Optional[str] = None
    parts: Optional[List[basicPart]] = None


class responseValidate(BaseModel):
    result: bool
    message: Optional[str] = None
