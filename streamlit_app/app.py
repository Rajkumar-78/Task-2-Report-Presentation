from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='Task 2 Sales Dashboard', layout='wide')
st.title('Task 2 — Sales Dashboard')
st.caption('Demo dashboard using synthetic sales data. Replace the CSV with your own data before submitting.')
DATA_PATH = Path(__file__).resolve().parents[1] / 'data' / 'sales_data.csv'
df = pd.read_csv(DATA_PATH)
df['revenue'] = df['units_sold'] * df['unit_price']
df['profit'] = df['units_sold'] * (df['unit_price'] - df['unit_cost'])

c1, c2 = st.columns(2)
with c1:
    st.subheader('Revenue by region')
    chart = df.groupby('region')['revenue'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    chart.plot(kind='bar', ax=ax)
    ax.set_xlabel('Region'); ax.set_ylabel('Revenue ($)')
    st.pyplot(fig)
with c2:
    st.subheader('Profit by product')
    chart = df.groupby('product')['profit'].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    chart.plot(kind='bar', ax=ax)
    ax.set_xlabel('Product'); ax.set_ylabel('Profit ($)')
    st.pyplot(fig)
st.subheader('Data preview')
st.dataframe(df, use_container_width=True)
