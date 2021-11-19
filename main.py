from flask import Flask, request
from flask import render_template

app = Flask("Hello World")


@app.route('/hello/', methods=['POST', 'GET'])
def finanzen():
    if request.method == 'POST':
        datum = request.form.get("datum")
        waehrung = request.form.get("waehrung")
        betrag = request.form.get("betrag")
        kategorie = request.form.get("kategorie")

        return datum, waehrung, betrag, kategorie
    else:
        return render_template('index.html')


@app.route('/einahmen/')
def einahmen():
    if request.method == 'POST':
        datum_1 = request.form.get("datum_1")
        waehrung_1 = request.form.get("waehrung_1")
        betrag_1 = request.form.get("betrag_1")
        kategorie_1 = request.form.get("kategorie_1")

        return datum_1, waehrung_1, betrag_1, kategorie_1
    else:
        return render_template('einahmen.html')


@app.route('/analyse/')
def analyse():
    return render_template('analyse.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
