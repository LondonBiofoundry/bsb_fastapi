import basicsynbio as bsb
from typing import Dict, Union
from app.schema import basicPart, basicPartType, fileType
from app.utils.basicPartFromFile import returnBasicPartFromUploadFileInitial


def jsonPartToBsbPart(
    jsonPart: basicPart, hashFileDict: Dict = None
) -> Union[bsb.BasicPart, str]:
    if jsonPart["type"] == basicPartType.collection:
        try:
            if jsonPart["collection"] == "BASIC_CDS_PARTS":
                return bsb.BASIC_CDS_PARTS[jsonPart["version"]][jsonPart["accessor"]]
            if jsonPart["collection"] == "BASIC_SEVA_PARTS":
                return bsb.BASIC_SEVA_PARTS[jsonPart["version"]][jsonPart["accessor"]]
            if jsonPart["collection"] == "BASIC_BIOLEGIO_LINKERS":
                return bsb.BASIC_BIOLEGIO_LINKERS[jsonPart["version"]][
                    jsonPart["accessor"]
                ]
            if jsonPart["collection"] == "BASIC_PROMOTER_PARTS":
                return bsb.BASIC_PROMOTER_PARTS[jsonPart["version"]][
                    jsonPart["accessor"]
                ]
            return "the part {jsonPart}: had a invalid collection"
        except Exception as e:
            return str(e)
    if jsonPart["type"] == basicPartType.uploadSingle:
        try:
            associatedFile = hashFileDict[jsonPart["fileId"]]
            print("associated filename", associatedFile.filename)
            bsbPart = returnBasicPartFromUploadFileInitial(
                associatedFile, fileType.genbank, jsonPart["addiseq"]
            )
            return bsbPart
        except Exception as e:
            return str(e)
    # else:
    #     if jsonPart["type"] == fileType.genbank:
    #         if jsonPart.multiple:
    #             mypart = returnBasicPartsFromUploadFileInitial(
    #                 jsonPart.base64, fileType.genbank, False
    #             )[jsonPart.index]
    #         else:
    #             print("Attempting to return basicpart from uploaded file")
    #             mypart = returnBasicPartFromUploadFileInitial(
    #                 jsonPart.base64, fileType.genbank, False
    #             )
    #     if jsonPart["type"] == fileType.fasta:
    #         if jsonPart.multiple:
    #             mypart = returnBasicPartsFromUploadFileInitial(
    #                 jsonPart.base64, fileType.fasta, False
    #             )[jsonPart.index]
    #         else:
    #             mypart = returnBasicPartFromUploadFileInitial(
    #                 jsonPart.base64, fileType.fasta, False
    #             )
    #     if jsonPart["type"] == fileType.SBOL:
    #         mypart = returnBasicPartFromUploadFileInitial(
    #             jsonPart.base64, fileType.SBOL, False
    #         )
    #     return mypart
