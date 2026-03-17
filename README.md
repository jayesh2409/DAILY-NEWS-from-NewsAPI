# DAILY-NEWS-from-NewsAPI

An Application for collecting daily news, storing the news data from NewsAPI globally into SQLitedatabase

Implementation of a Streamlit dashboard for visualizing the data from the database

Work flow:

News headline -> TextBlob Sentiment Analysis -> Sentiment score generated -> Stored in SQLite database -> Displayed in Streamlit dashboard

Sentiment Analysis: Applied to each unique news using TextBlob to determine whether the news expresses a positive, negative, or neutral sentiment, and the resulting polarity score is stored in the database
