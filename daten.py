import json


# Speichern der Ausgaben in JSON Datei
def ausgaben_speichern(datum, waehrung, betrag, kategorie):
    datei = "ausgaben.json"
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {
            "Datum": datum,
            "Waehrung": waehrung,
            "Betrag": betrag,
            "Kategorie": kategorie
        }

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


# Speichern der Einahmen in JSON Datei
def einahmen_speichern(datum_1, waehrung_1, betrag_1, kategorie_1):
    datei = "einahmen.json"
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {
            "Datum": datum_1,
            "Waehrung": waehrung_1,
            "Betrag": betrag_1,
            "Kategorie": kategorie_1
        }

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


def suche(suchbegriff):
    with open("ausgaben.json") as datei_name:
        json_as_string = datei_name.read()
        my_read_dict = json.loads(json_as_string)
        if suchbegriff in my_read_dict.keys():
            result = my_read_dict[suchbegriff]
        else:
            result = "Nein"
        return result


# Laden des kompletten Inhaltes einer Datei.
def alles(datei):
    with open(datei) as datei_name:
        json_as_string = datei_name.read()
        my_read_dict = json.loads(json_as_string)
        return my_read_dict

# if shopping > 200:
# print (shopping - 200, "sind unnötige Ausgaben)
