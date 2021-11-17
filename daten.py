from datetime import datetime
import json


def speichern(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(key)] = value

    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


def ausgaben_speichern(ausgaben):
    datei_name = "ausgaben_1.json"
    zeitpunkt = datetime.now()
    speichern(datei_name, zeitpunkt, ausgaben)
    return zeitpunkt, ausgaben


def ausgaben_laden():
    datei_name = "ausgaben_1.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt

#if shopping > 200:
# print (shopping - 200, "sind unnötige Ausgaben)