import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("news.db")

df = pd.read_sql("SELECT * FROM news", conn)

st.title("AI Daily News Dashboard")

st.write("Latest News Data")
st.dataframe(df)

st.write("Sentiment Distribution")
st.bar_chart(df["sentiment"])