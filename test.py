import json


def rechnen():
    with open('ausgaben.json') as openfile:
        daten = json.load(openfile)

    liste = []

    for summe in daten:
        if summe['Kategorie'] == "Shopping":
            liste.append(float(summe['Betrag']))
    myliste = sum(liste)
    print(myliste)