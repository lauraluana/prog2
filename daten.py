import json


# Quelle für das Öffnen der Datei (json.load, usw.) sind die Vorlesungsunterlagen.

# Speichern der Ausgaben in JSON Datei
def ausgaben_speichern(datum, waehrung, betrag, kategorie):
    datei = "ausgaben.json"
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[str(datum)] = {
        "Datum": datum,
        "Waehrung": waehrung,
        "Betrag": betrag,
        "Kategorie": kategorie,
    }

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


# Suchfunktion, welche die Keys des Dictionary nach dem Suchbegriff durchsucht
# Wenn dieser exakt gefunden wird, wird das entsprechende Dictionary als Resultat zurückgegeben.
# Ansonsten wird die Meldung, dass kein Eintrag gefunden wurde, zurückgegeben.
def suche(suchbegriff):
    with open("ausgaben.json") as datei_name:
        json_as_string = datei_name.read()
        my_read_dict = json.loads(json_as_string)
        if suchbegriff in my_read_dict.keys():
            result = my_read_dict[suchbegriff]
        else:
            result = "Nein"
        return result


# Speichern der Einahmen in der JSON Datei
def einahmen_speichern(datum, waehrung, betrag, kategorie):
    datei = "einahmen.json"
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    if str(kategorie) in datei_inhalt:
        datei_inhalt[str(kategorie)] = {
            "Datum": datum,
            "Waehrung": waehrung,
            "Betrag": betrag,
        }
    else:
        datei_inhalt[str(kategorie)] = {}
        datei_inhalt[str(kategorie)] = {
            "Datum": datum,
            "Waehrung": waehrung,
            "Betrag": betrag,
        }

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)


# Laden des kompletten Inhaltes einer Datei.
# Wird verwendet für die Approutes "Allepersonen" und "Allelogs".
def alles(datei):
    with open(datei) as datei_name:
        json_as_string = datei_name.read()
        my_read_dict = json.loads(json_as_string)
        return my_read_dict

# if shopping > 200:
# print (shopping - 200, "sind unnötige Ausgaben)
