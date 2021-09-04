from app.utils.ItemtoPart import itemtopart


def return_sequence_annotations(item, Qualifier):
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

    mypart = itemtopart(item)
    annotations = map(extract_feature, mypart.features)

    return {"annotated": list(annotations), "seq": str(mypart.seq)}
