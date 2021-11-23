def extract_feature(item):
    if item.qualifiers["label"][0]:
        name = item.type + ":" + item.qualifiers["label"][0]
    else:
        name = item.type
    return {
        "start": item.location.start,
        "end": item.location.end,
        "name": name,
        "direction": item.strand,
    }
