from app.utils.ItemtoPart import itemtopart
from fastapi.logger import logger

def get_qualifiers(item):
    return list(item.qualifiers)[0]


def viewpartlabels(mypart):
    if mypart:
        print('mypart',mypart)
        bsbpart = itemtopart(mypart)
        print(bsbpart)

        options = list(set(map(get_qualifiers, bsbpart.features)))
    else:
        options = []
    options.append("Feature")
    return options
