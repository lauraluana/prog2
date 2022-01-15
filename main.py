from flask import Flask, request
from flask import render_template
import daten
import analyse
import json
from plotly.offline import plot

app = Flask("Hello World")


# Für den Aufbau der main Seite wurde vorallem die Folie PRO2.2 Flask und Jinja2 benutzt
@app.route('/hello/', methods=['POST', 'GET'])
def finanzen():
    #
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


@app.route('/analyse/', methods=['POST', 'GET'])
# Quelle: Pro2-Demos Kapitel 11 Datenvisualisierung
def viz():
    if request.method == 'POST':
        abfrage = request.form.get("kategorie")
        # Das vordefinierte Diagram auf analyse.py wird hier definiert.
        fig = analyse.diagram(abfrage)
        div = plot(fig, output_type="div")
        # Hier soll die Abbildung des Diagrams auf der analyse.html seite stattfinden, sowie die Berechnung der Summe
        return render_template('analyse.html', viz_div=div)
    # Falls keine Daten mitgeschickt werden, soll False an den Stellen vom Diagram sowie der am Ende der Berechnung
    return render_template('analyse.html', viz_div=False)


@app.route('/liste/')
def rechnen():
    with open('ausgaben.json') as openfile:
        daten = json.load(openfile)

        liste = []

        for summe in daten:
            if summe['Kategorie'] == "Lebensmittel":
                liste.append(float(summe['Betrag']))
        myliste = sum(liste)
    return render_template('liste.html', name=myliste)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
