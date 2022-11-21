import streamlit as st
from multiapp import MultiApp
from apps import home, sentiment_2 ,sentiment_1, sentiment_0 # import your app modules here

app = MultiApp()

st.markdown("""
# Amazon Reviews Sentiment Analyzer

This Amazon Reviews Sentiment Analyzer app is using the [Vader Sentiment Python Library](https://github.com/cjhutto/vaderSentiment).

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Web Scrapping", sentiment_2.app)
app.add_app("Online Review Analyzer", sentiment_1.app)
app.add_app("Text Review Analyzer", sentiment_0.app)
# The main app
app.run()
