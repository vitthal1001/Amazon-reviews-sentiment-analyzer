from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.in/Alchemist-Paulo-Coelho/product-reviews/8172234988/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
reviewlist = []

def get_soup(url):
    r = requests.get("https://www.amazon.in/Alchemist-Paulo-Coelho/product-reviews/8172234988/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews")
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = {
            'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
            'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass
    
soup=get_soup("https://www.amazon.in/Alchemist-Paulo-Coelho/product-reviews/8172234988/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews")
get_reviews(soup)
print(len(reviewlist))


for x in range(1,170):
    soup = get_soup(f"https://www.amazon.in/Alchemist-Paulo-Coelho/product-reviews/8172234988/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews")
    print(f'Getting page: {x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break

import pandas as pd
df = pd.DataFrame(reviewlist)