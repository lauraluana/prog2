from flask import Flask, request
from flask import render_template
import daten
import analyse
import json
from plotly.offline import plot

app = Flask("Hello World")


# Für den Aufbau der main Seite wurde vorallem die Folie PRO2.2 Flask und Jinja2 benutzt

# Ist die Startseite, welche die Möglichkeit bietet die Ausgaben einzugeben
@app.route('/hello/', methods=['POST', 'GET'])
def finanzen():
    # Hier werden die eingegebenen Ausgaben definiert
    if request.method == 'POST':
        date = request.form.get("datum")
        waehrung = request.form.get("waehrung")
        betrag = request.form.get("betrag")
        kategorie = request.form.get("kategorie")
        # Die Daten die im Formular angegeben wurden, werden im "ausgaben.json" gespeichert
        daten.speichern("ausgaben.json", date, waehrung, betrag, kategorie)
        # Es wird das Formular mit den Eingaben an den Nutzer zurückgeschickt, falls das Formular ausgefüllt wurde.
        return render_template('erfasst.html', titel="Ausgaben", datum=date, waehrung=waehrung, betrag=betrag,
                               kategorie=kategorie)
    else:
        # Es wird das entsprechende HTML angezeigt,falls das Formular nicht ausgefüllt wurde.
        return render_template('index.html')


@app.route('/einahmen/', methods=['POST', 'GET'])
def einahmen():
    # Hier werden die eingegebenen Ausgaben definiert
    if request.method == 'POST':
        datum = request.form.get("datum")
        waehrung = request.form.get("waehrung")
        betrag = request.form.get("betrag")
        kategorie = request.form.get("kategorie")
        # Die Daten die im Formular angegeben wurden, werden im "einahmen.json" gespeichert
        daten.speichern("einnahmen.json", datum, waehrung, betrag, kategorie)
        # Es wird das Formular mit den Eingaben an den Nutzer zurückgeschickt, falls das Formular ausgefüllt wurde.
        return render_template('erfasst.html', titel="Einnahmen", datum=datum, waehrung=waehrung, betrag=betrag,
                               kategorie=kategorie)

    else:
        # Es wird das entsprechende HTML angezeigt,falls das Formular nicht ausgefüllt wurde.
        return render_template('einahmen.html')


# Quelle: Pro2-Demos Kapitel 11 Datenvisualisierung
@app.route('/analyse/', methods=['POST', 'GET'])
def viz():
    if request.method == 'POST':
        # Die im analyse.html ausgewählte Kategorie wird hier aufgenommen
        abfrage = request.form.get("kategorie")
        # Das vordefinierte Diagram auf analyse.py wird hier definiert.
        fig = analyse.diagram(abfrage)
        div = plot(fig, output_type="div")
        # Hier soll die Abbildung des Diagrams auf der analyse.html Seite stattfinden
        return render_template('analyse.html', viz_div=div)
    # Falls keine Daten mitgeschickt werden, soll False an den Stellen vom Diagram ein False stehen
    return render_template('analyse.html', viz_div=False)


# Auf dieser Seite wird die Summe aller Ausgaben in der Kategorie "Shopping" abgebildet.
@app.route('/liste/')
def liste_laden():
    # Es werden zuerst die gesammelten Daten aus der Datei "ausgaben.json" geladen
    with open('ausgaben.json') as openfile:
        daten = json.load(openfile)
        # Die Liste ist zuerst leer, da die gewünschten Daten zuerst gefiltert werden müssen
        liste = []

        for summe in daten:
            # Wenn die Kategorie = Shopping ist, wird die If Schleife ausgeführt.
            if summe['Kategorie'] == "Shopping":
                # Alle Beträge die zur Kategorie "Shopping" gehören, werden in die Liste aufgenommen
                liste.append(float(summe['Betrag']))
                # Alle Beträge werden mit dem Befehl "sum" zusammengezählt
        myshop = sum(liste)

        for summe in daten:
            # Wenn die Kategorie = Shopping ist, wird die If Schleife ausgeführt.
            if summe['Kategorie'] == "Tanken":
                # Alle Beträge die zur Kategorie "Tanken" gehören, werden in die Liste aufgenommen
                liste.append(float(summe['Betrag']))
                # Alle Beträge werden mit dem Befehl "sum" zusammengezählt
        mytank = sum(liste)

        for summe in daten:
            # Wenn die Kategorie = Shopping ist, wird die If Schleife ausgeführt.
            if summe['Kategorie'] == "Lebensmittel":
                # Alle Beträge die zur Kategorie "Lebensmittel" gehören, werden in die Liste aufgenommen
                liste.append(float(summe['Betrag']))
                # Alle Beträge werden mit dem Befehl "sum" zusammengezählt
        mylebmi = sum(liste)

        for summe in daten:
            # Wenn die Kategorie = Shopping ist, wird die If Schleife ausgeführt.
            if summe['Kategorie'] == "Freizeit":
                # Alle Beträge die zur Kategorie "Freizeit" gehören, werden in die Liste aufgenommen
                liste.append(float(summe['Betrag']))
                # Alle Beträge werden mit dem Befehl "sum" zusammengezählt
        myliste = sum(liste)

        # Die Summe der Liste erscheint im HTML "Liste"
    return render_template('liste.html', name=myshop, name1=mytank, name2=mylebmi, name3=myliste)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
