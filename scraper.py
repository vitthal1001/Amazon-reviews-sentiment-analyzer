from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


class Scrapper:
    reviewlist = []
    def __init__(self, url):
        self.url = url
    
    def get_soup(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup
    
    def get_reviews(self):
        soup = self.get_soup()
        reviews = soup.find_all('div', {'data-hook': 'review'})
        try:
            for item in reviews:
                review = {
                    'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
                    'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
                    'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
                    }
                Scrapper.reviewlist.append(review)
        except:
            pass

    def FinalDataFrame(self):
        for x in range(1,20):
            soup = self.get_soup()
            print(f'Getting page: {x}')
            self.get_reviews()
            print(len(Scrapper.reviewlist))
            if not soup.find('li', {'class': 'a-disabled a-last'}):
                pass
            else:
                break
        df = pd.DataFrame(Scrapper.reviewlist)
        return df 

url = "https://www.amazon.in/Alchemist-Paulo-Coelho/product-reviews/8172234988/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
sc = Scrapper(url)
df = sc.FinalDataFrame()
print(df)
df.to_csv('D:/Web_App_Deployment/amazon_reviews_1.csv', index=False) 


# url = "https://www.amazon.in/Alchemist-Paulo-Coelho/product-reviews/8172234988/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
# reviewlist = []

# def get_soup(url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'html.parser')
#     return soup

# def get_reviews(soup):
#     reviews = soup.find_all('div', {'data-hook': 'review'})
#     try:
#         for item in reviews:
#             review = {
#             'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
#             'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
#             'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
#             }
#             reviewlist.append(review)
#     except:
#         pass


# soup=get_soup(url)
# get_reviews(soup)
# print(len(reviewlist))

# for x in range(1,5):
#     soup = get_soup(url)
#     print(f'Getting page: {x}')
#     get_reviews(soup)
#     # print(len(reviewlist))
#     if not soup.find('li', {'class': 'a-disabled a-last'}):
#         pass
#     else:
#         break

# df = pd.DataFrame(reviewlist)
# print(df)