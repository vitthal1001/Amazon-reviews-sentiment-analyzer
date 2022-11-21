import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#from pickle import dump,load
import requests
from bs4 import BeautifulSoup

def app():

    def fetch_data():
        link=st.text_input("Enter product review link")
        url=link
        if not url:
            st.stop()
        if url:   
            r = requests.get(url)
            # Parsing the HTML content
            soup = BeautifulSoup(r.text, 'html.parser')

            # Getting desired data from our parsed soup
            reviews = soup.find_all('div', {'data-hook': 'review'})
            
            # Initialize list
            reviewlist = []
            
            def get_soup(url):
                r = requests.get(url,params={'url': url, 'wait': 5})
                soup = BeautifulSoup(r.text, 'html.parser')
                return soup
                    
                df = pd.DataFrame(reviewlist)
            
            # Initialize list to store reviews data later on
            reviewlist = []
                
            # Function 2: look for web-tags in our soup, then append our data to reviewList
            def get_reviews(soup):
                reviews = soup.find_all('div', {'data-hook': 'review'})
                try:
                    for item in reviews:
                        review = {
                            'product': soup.title.text.replace('Amazon.ca:Customer reviews: ', '').strip(), 
                            'date': item.find('span', {'data-hook': 'review-date'}).text.strip(),
                            'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
                            'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
                            'review_list': item.find('span', {'data-hook': 'review-body'}).text.strip(),
                        }
                        reviewlist.append(review)
                except:
                    pass
                
            for x in range(0,100):
                soup = get_soup(url)
                get_reviews(soup)
                if not soup.find('li', {'class': 'a-disabled a-last'}):
                    pass
                else:
                    break

            df = pd.DataFrame(reviewlist)        
            return df 

    def main():
        df1 = fetch_data()
        # #st.download_button(label="Download data as CSV", data=csv, file_name='Amazon_Reviews.csv',mime='text/csv')
        # #if st.button('Download file as csv'):
        df1.to_csv(r'Amazon_reviews.csv', index=False)
        

    main()

if __name__ == '__app__':
    app()