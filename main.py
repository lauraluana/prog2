from flask import Flask, request
from flask import render_template
import daten
import analyse
import matplotlib.pyplot as plt

app = Flask("Hello World")


@app.route('/hello/', methods=['POST', 'GET'])
def finanzen():
    if request.method == 'POST':
        date = request.form.get("datum")
        waehrung = request.form.get("waehrung")
        betrag = request.form.get("betrag")
        kategorie = request.form.get("kategorie")
        daten.speichern("ausgaben.json", date, waehrung, betrag, kategorie)
        return render_template('erfasst.html', titel="Ausgaben", datum=date, waehrung=waehrung, betrag=betrag,
                               kategorie=kategorie)
    else:
        return render_template('index.html')


@app.route('/einahmen/', methods=['POST', 'GET'])
def einahmen():
    if request.method == 'POST':
        datum = request.form.get("datum")
        waehrung = request.form.get("waehrung")
        betrag = request.form.get("betrag")
        kategorie = request.form.get("kategorie")
        daten.speichern("einnahmen.json", datum, waehrung, betrag, kategorie)
        return render_template('erfasst.html', titel="Einnahmen", datum=datum, waehrung=waehrung, betrag=betrag,
                               kategorie=kategorie)
    else:
        return render_template('einahmen.html')


@app.route('/analyse/', methods=['POST', 'GET'])
def viz():
    if request.method == 'POST':
        kategorie = request.form.get("kategorie")
    return render_template('analyse.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
