# app/utils.py
import pandas as pd

def load_data():
    benin = pd.read_csv('data/benin_clean.csv')
    togo = pd.read_csv('data/togo_clean.csv')
    sl = pd.read_csv('data/sierra_leone_clean.csv')

    benin['Country'] = 'Benin'
    togo['Country'] = 'Togo'
    sl['Country'] = 'Sierra Leone'

    return pd.concat([benin, togo, sl], ignore_index=True)
