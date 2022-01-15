import pandas as pd


def main(json_file):
    df = pd.read_json(json_file)
    df.to_json("ausgaben.json")
