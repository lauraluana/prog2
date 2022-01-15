import json
import matplotlib.pyplot as plt

with open('ausgaben.json') as openfile:
    daten = json.load(openfile)

xwerte = []
ywerte = []

for eintrag in daten:
    if eintrag['Kategorie'] == 'Lebensmittel':
        xwerte.append(eintrag['Datum'])
        ywerte.append(float(eintrag['Betrag']))

plt.bar(xwerte, ywerte, color='#557f2d')
plt.style.use('seaborn-darkgrid')
palette = plt.get_cmap('Set1')

plt.title("Übersicht CHF Ausgaben", loc='center', fontsize=12, fontweight=0, color='black')
plt.xlabel("Datum")
plt.ylabel("Betrag")

plt.show()

