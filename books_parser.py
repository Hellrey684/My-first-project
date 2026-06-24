import requests
from bs4 import BeautifulSoup
import csv

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
all_books = []
page = 1

while True:
    url = base_url.format(page)
    response = requests.get(url)
    if response.status_code != 200:
        print('Error loading page')
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')

    if not books:
        print('No books found')
        break

    for book in books:
        title_tag = book.find('h3').find('a')
        title = title_tag.text if title_tag else None
        price = book.find('p', class_='price_color').get_text()
        rating_tag = book.find('p', class_='star-rating')
        rating = rating_tag['class'][1] if rating_tag else None
        all_books.append([title, price, rating])

    page += 1

with open('all_books.csv', 'w', newline='', encoding='utf-8') as f:
    csv.writer(f).writerow(['Title', 'Price', 'Rating'])
    csv.writer(f).writerows(all_books)

print(f"Done! Collected {len(all_books)} books.")