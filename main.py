from flask import Flask
from flask import render_template
import daten

app = Flask("Hello World")


@app.route('/hello/')
def finanzen():
    return render_template('index.html')


@app.route("/speichern/<ausgaben>")
def speichern(ausgaben):
    zeitpunkt, ausgaben = daten.ausgaben_speichern(ausgaben)

    return "Gespeichert: " + ausgaben + " um " + str(zeitpunkt)


@app.route("/liste")
def auflisten():
    ausgaben = daten.ausgaben_laden()

    ausgaben_liste = ""
    for key, value in ausgaben.items():
        zeile = str(key) + ": " + value + "<br>"
        ausgaben_liste += zeile

    return ausgaben_liste

def ausgaben_laden():
    datei_name = "aktivitaeten.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt


if __name__ == '__main__':
    app.run(debug=True, port=5000)
