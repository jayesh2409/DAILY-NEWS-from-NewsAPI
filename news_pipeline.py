import requests
import pandas as pd
import sqlite3
from textblob import TextBlob
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

url = "https://newsapi.org/v2/top-headlines"

params = {
    "country": "us",
    "apiKey": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

articles = []

for article in data["articles"]:
    title = article["title"]

    sentiment = TextBlob(title).sentiment.polarity

    articles.append({
        "title": title,
        "source": article["source"]["name"],
        "published": article["publishedAt"],
        "sentiment": sentiment,
        "timestamp": datetime.now()
    })

df = pd.DataFrame(articles)

conn = sqlite3.connect("news.db")

df.to_sql("news", conn, if_exists="append", index=False)

conn.close()

print("News data stored successfully")