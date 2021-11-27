from app.utils.ItemtoPart import itemtopart
from fastapi.logger import logger


def get_qualifiers(item):
    return list(item.qualifiers)[0]


def viewpartlabels(mypart):
    if mypart:
        bsbpart = itemtopart(mypart)

        options = list(set(map(get_qualifiers, bsbpart.features)))
    else:
        options = []
    options.append("Feature")
    return options
