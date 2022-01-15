import pandas as pd

def laden():

    df = pd.DataFrame(
        {
            "Datum": ["2022-01-15", "2021-12-29", "2021-12-10", "2021-11-11", "2021-10-25"],
            "Waehrung": ["CHF", "CHF", "CHF", "CHF", "CHF"],
            "Betrag": [20, 12, 267.35, 970, 78],
            "Kategorie": ["Tanken", "Lebensmittel", "Freizeit", "Shopping", "Tanken"]
        }
    )
    return df
