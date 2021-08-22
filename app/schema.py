from pydantic import BaseModel
from typing import Optional, List


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
