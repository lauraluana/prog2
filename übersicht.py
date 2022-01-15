import pandas as pd
import json

def sachen_laden(json_file):
    df = pd.read_json(json_file)
    df.to_json("ausgaben.json")
    print(df.describe())









