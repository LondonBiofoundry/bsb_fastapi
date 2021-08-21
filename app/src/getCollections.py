import basicsynbio as bsb
from app.utils.partToString import partToString


def getCollections():
    collections = [x for x in dir(bsb) if x.startswith("BASIC_")]
    apiresponse = []
    for collection in collections:
        apicollection = {"name": collection}
        bsbcollection = getattr(bsb, collection)
        versions = list(bsbcollection.keys())
        for version in versions:
            bsbversion = bsbcollection[version]
            apicollection[version] = [
                {
                    "label": bsbversion[item].name,
                    "accessor": item,
                    "binaryString": partToString(bsbversion[item]),
                    "description": bsbversion[item].description,
                    "collection": collection,
                }
                for item in bsbversion
            ]
        apiresponse.append(apicollection)
    return apiresponse
