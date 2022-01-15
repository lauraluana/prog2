import json

import plotly.express as px


def diagram(abfrage):
    with open('ausgaben.json') as openfile:
        daten = json.load(openfile)

    xwerte = []
    ywerte = []

    for eintrag in daten:
        if eintrag['Kategorie'] == abfrage:
            xwerte.append(eintrag['Datum'])
            ywerte.append(float(eintrag['Betrag']))

    fig = px.bar(xwerte, ywerte)

def rechnen(abfrage):
    with open('ausgaben.json') as openfile:
        daten = json.load(openfile)

    liste = []

    for summe in daten:
        if summe['Kategorie'] == abfrage:
            liste.append(float(summe['Betrag']))
    myliste = sum(liste)
    return myliste
