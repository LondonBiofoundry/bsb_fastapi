from typing import Dict
from app.schema import basicPart

from app.utils.jsonPartToBsbPart import jsonPartToBsbPart


def get_qualifiers(item):
    return list(item.qualifiers)[0]


def viewpartlabels(part: basicPart, hashFileDictionary: Dict = None):
    try:
        if part:
            bsbPart = jsonPartToBsbPart(part, hashFileDictionary)
            options = list(set(map(get_qualifiers, bsbPart.features)))
            options.append("Feature")
            return {"result": True, "message": options}
        else:
            return {"result": False, "message": "No part supplied"}
    except Exception:
        return {"result": False, "message": "No part supplied"}
