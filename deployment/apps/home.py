import streamlit as st

def app():
    st.title('Home')

    st.write('This is the `home page` of this Amazon reviews Sentiment Analyzer app.')

    st.write('In this app, we will be analyzing amazon reviews data using the Vader Sentiment python library.')
             
    st.sidebar.subheader("About the Model")
    st.sidebar.text('''VADER Sentiment - 
    (Valence Aware Dictionary 
    And Sentiment Reasoner) 
    BASED SENTIMENT ANLYSIS''')

    st.sidebar.subheader("By Vitthal Choudhari")