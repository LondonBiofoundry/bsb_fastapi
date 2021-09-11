from pydantic import BaseModel
from typing import Optional, List, Any
from enum import Enum
from fastapi import File, UploadFile
from app.schema_examples.exampleBasicBuild import exampleBasicBuild
from app.schema_examples.exampleBasicPart import exampleBasicPart


class basicPart(BaseModel):
    id: Optional[str] = None
    accessor: Optional[str] = None
    binaryString: Optional[str] = None
    base64: Optional[Any] = None
    collection: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    label: Optional[str] = None
    multiple: Optional[bool] = None
    index: Optional[int] = None
    type: Optional[str] = None

    class Config:
        schema_extra = {"example": exampleBasicPart}


class basicBuild(BaseModel):
    id: str
    name: Optional[str] = None
    description: Optional[str] = None
    parts: Optional[List[basicPart]] = None

    class Config:
        schema_extra = {"example": exampleBasicBuild}


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
