import json
import matplotlib.pyplot as plt

# Quelle: https://im-coder.com/python-matplotlib-mehrere-balken.html
# Quelle: https://www.python-graph-gallery.com/barplot/


def diagram(abfrage):
    # Die Daten werden aus der Json Datei "ausgaben.json" geladen
    with open('ausgaben.json') as openfile:
        daten = json.load(openfile)
# Um die gewünschten Daten zu erhalten, muss zuerst gefiltert werden
    xwerte = []
    ywerte = []


    for eintrag in daten:
        # Sobald die Kategorie = der in analyse.html ausgesuchte Kategorie ist wird die if-Funktion ausgeführt
        if eintrag['Kategorie'] == abfrage:
            # In den unteren zwei Zeilen, werden die entsprechenden Werte in die leeren Listen eingeführt
            xwerte.append(eintrag['Datum'])
            # Der Betrag wird als float hinzugefügt, da bei den Ausgaben meistens zu Beträge mit Kommas kommt
            ywerte.append(float(eintrag['Betrag']))
# Definition was im Balkendiagram dargestellt werden soll
    plt.bar(xwerte, ywerte, color='#557f2d')

    plt.title("Übersicht CHF Ausgaben", loc='center', fontsize=12, fontweight=0, color='black')
    plt.xlabel("Datum")
    plt.ylabel("Betrag")
