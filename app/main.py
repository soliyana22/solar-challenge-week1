import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    benin = pd.read_csv('data/benin_clean.csv')
    togo = pd.read_csv('data/togo_clean.csv')
    sl = pd.read_csv('data/sierra_leone_clean.csv')

    benin['Country'] = 'Benin'
    togo['Country'] = 'Togo'
    sl['Country'] = 'Sierra Leone'

    return pd.concat([benin, togo, sl], ignore_index=True)

df = load_data()

# Sidebar
countries = st.multiselect("Select countries", df['Country'].unique(), default=df['Country'].unique())
metric = st.selectbox("Choose a metric", ['GHI', 'DNI', 'DHI'])

df_filtered = df[df['Country'].isin(countries)]

# Boxplot
st.subheader(f"{metric} Comparison")
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df_filtered, x='Country', y=metric, palette='Set3', ax=ax)
st.pyplot(fig)
