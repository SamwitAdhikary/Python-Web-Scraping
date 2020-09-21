import requests
from bs4 import BeautifulSoup 
import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    url = f'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = '_1-2Iqu')
    for item in divs:
        title = item.find('div', class_ = '_3wU53n').text
        price = item.find('div', class_ = '_1vC4OE').text.replace('₹', '')
        reviews = item.find('div', class_ = 'hGSR34').text
        # features = item.find('div', {'class': '_3ULzGw'}).text

        mobile = {
            'Name': title,
            'Price': price,
            'Reviews': reviews,
            # 'Features': features,
        }

        mob_list.append(mobile)
    return


mob_list = [] 

for i in range(1,14):
    print(f'Scraping Page {i}!!')
    c = extract(i)
    transform(c)
# print(len(mob_list))
df = pd.DataFrame(mob_list)
print(df.head())

df.to_csv('mobile.csv')
