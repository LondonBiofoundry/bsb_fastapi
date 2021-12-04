import basicsynbio as bsb
from app.schema import basicPartType
from app.utils.partToString import partToString


def getCollections():
    collections = [x for x in dir(bsb) if x.startswith("BASIC_")]
    print("collections", collections)
    apiresponse = []
    for collection in collections:
        bsbcollection = getattr(bsb, collection)
        versions = list(bsbcollection.keys())
        apicollection = {
            "name": collection,
            "availableVersions": versions,
            "versions": [
                {
                    "name": version,
                    "parts": [
                        {
                            "id": bsbcollection[version][item].id,
                            "type": basicPartType.collection,
                            "label": bsbcollection[version][item].name
                            or "defalt-label",
                            "accessor": item or "defalt-label",
                            "description": bsbcollection[version][item].description
                            or "defalt-label",
                            "collection": collection or "defalt-label",
                            "version": version or "defalt-label",
                            "seq": str(bsbcollection[version][item].seq)
                            or "defalt-label",
                        }
                        for item in bsbcollection[version]
                    ],
                }
                for version in versions
            ],
        }
        apiresponse.append(apicollection)
    return apiresponse
