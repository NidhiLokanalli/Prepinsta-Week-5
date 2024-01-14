
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://books.toscrape.com/'

response = requests.get(url)
response

response.status_code

type(response)

print(response.text[:1000])

type(response.text)

soup = BeautifulSoup(response.text)
type(soup)

books_tag = soup.find_all('article',class_='product_pod')

len(books_tag)

book = books_tag[19]
print(book)

title_tag = book.find('a',title=True)['title']
title_tag

rating_tag = book.find('p')['class'][1]
rating_tag

price_tag = book.find('p',class_='price_color').text[1:]
price_tag

link_tag = 'http://books.toscrape.com/' + book.find('a')['href']
link_tag

data_list = []

for books in range(0, 20):
  book = books_tag[books]
  title_tag = book.find('a',title=True)['title']
  rating_tag = book.find('p')['class'][1]
  price_tag = book.find('p',class_='price_color').text[1:]
  link_tag = 'http://books.toscrape.com/' + book.find('a')['href']

  data_list.append([title_tag, price_tag, rating_tag, link_tag])

columns = ['Title', 'Price', 'Rating', 'Link']
df = pd.DataFrame(data_list, columns=columns)

df

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

num_pages = 5

data_list = []
# Loop through pages
for page_number in range(1, num_pages + 1):

  # Constructing URL for each page
  url = base_url.format(page_number)

  # Make an HTTP request and create BeautifulSoup object
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  # Find all book articles on the page
  books_tag = soup.find_all('article', class_='product_pod')

  # Extract data for each book on the page
  for book in books_tag:
    title_tag = book.find('a', title=True)['title']
    rating_tag = book.find('p')['class'][1]
    price_tag = book.find('p', class_='price_color').text[1:]
    link_tag = 'http://books.toscrape.com/' + book.find('a')['href']

    # Append the data to the list
    data_list.append([title_tag, price_tag, rating_tag, link_tag])



columns = ['Title', 'Price', 'Rating', 'Link']
complete_df = pd.DataFrame(data_list, columns=columns)

complete_df
complete_df.shape
complete_df.to_csv('books_data.csv', index=False)