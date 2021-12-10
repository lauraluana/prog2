import json


# Speichern der Ausgaben in JSON Datei
def speichern(datei, datum, waehrung, betrag, kategorie):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = []

    datei_inhalt.append({
        "Datum": datum,
        "Waehrung": waehrung,
        "Betrag": betrag,
        "Kategorie": kategorie
    })

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

