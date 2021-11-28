from typing import Dict
from app.schema import basicPart
from app.utils.jsonPartToBsbPart import jsonPartToBsbPart


def return_sequence_annotations(
    jsonPart: basicPart, Qualifier: str, hashFileDictionary: Dict = None
):
    def extract_feature(myfeature):
        try:
            # myfeature.qualifiers[Qualifier][0]:
            name = myfeature.qualifiers[Qualifier][0]
            try:
                last_location = myfeature.location.parts[0]
                return {
                    "start": last_location.start,
                    "end": last_location.end,
                    "name": name,
                    "direction": last_location.strand,
                }
            except:
                return {
                    "start": myfeature.location.start,
                    "end": myfeature.location.end,
                    "name": name,
                    "direction": myfeature.strand,
                }
        except:
            return

    try:
        bsbPart = jsonPartToBsbPart(jsonPart, hashFileDictionary)
        annotations = map(extract_feature, bsbPart.features)
        return {"annotations": list(annotations)}
    except:
        return {"annotations": []}
