from export_empl import export_dt
from import_empl import import_dt


def search_dt(word, data):
    if len(data) > 0:
        for i in data:
            if word in i:
                return i
    else:
        return None
