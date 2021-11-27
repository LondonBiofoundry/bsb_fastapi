import basicsynbio as bsb

from app.schema import basicPart, fileType
from app.utils.basicPartFromFile import (
    returnBasicPartsFromUploadFileInitial,
    returnBasicPartFromUploadFileInitial,
)


def itemtopart(item: basicPart):
    if item.collection == "BASIC_CDS_PARTS":
        return bsb.BASIC_CDS_PARTS["v0.1"][item.accessor]
    if item.collection == "BASIC_SEVA_PARTS":
        return bsb.BASIC_SEVA_PARTS["v0.1"][item.accessor]
    if item.collection == "BASIC_BIOLEGIO_LINKERS":
        return bsb.BASIC_BIOLEGIO_LINKERS["v0.1"][item.accessor]
    if item.collection == "BASIC_PROMOTER_PARTS":
        return bsb.BASIC_PROMOTER_PARTS["v0.1"][item.accessor]
    else:
        if item.type == fileType.genbank:
            if item.multiple:
                mypart = returnBasicPartsFromUploadFileInitial(
                    item.base64, fileType.genbank, False
                )[item.index]
            else:
                print("Attempting to return basicpart from uploaded file")
                mypart = returnBasicPartFromUploadFileInitial(
                    item.base64, fileType.genbank, False
                )
        if item.type == fileType.fasta:
            if item.multiple:
                mypart = returnBasicPartsFromUploadFileInitial(
                    item.base64, fileType.fasta, False
                )[item.index]
            else:
                mypart = returnBasicPartFromUploadFileInitial(
                    item.base64, fileType.fasta, False
                )
        if item.type == fileType.SBOL:
            mypart = returnBasicPartFromUploadFileInitial(
                item.base64, fileType.SBOL, False
            )
        return mypart
