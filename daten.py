import json


# Speichern der Ausgaben in JSON Datei
# Quelle: Programmieren 1, PRO1.7 - Input and Output
def speichern(datei, datum, waehrung, betrag, kategorie):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
            # Falls noch keine Json Datei vorhanden ist
            # Hilfe von Isabelle Köhle betreffend FileNotFoundError
    except FileNotFoundError:
        # Wenn keine Json Datei vorhanden ist, ist der Inhalt natürlich leer
        datei_inhalt = []
# Hier wird festgelegt, was in die Jason Datei hinzugefügt werden soll
    datei_inhalt.append({
        "Datum": datum,
        "Waehrung": waehrung,
        "Betrag": betrag,
        "Kategorie": kategorie
    })

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

