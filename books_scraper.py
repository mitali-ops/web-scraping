
import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Scraping book data from all pages on the books website...
")
total_pages = 50  # Total number of pages to scrape
books_data = []  # List to store book information

# Loop through all pages
for page in range(1, total_pages + 1):
    books_url = f'http://books.toscrape.com/catalogue/page-{page}.html'
    response = requests.get(books_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all book entries on the current page
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        book_title = book.h3.a['title']  # Book title
        book_price = book.find('p', class_='price_color').get_text()  # Book price
        availability = book.find('p', class_='instock availability').get_text(strip=True)  # Availability status

        # Append book details to the list
        books_data.append({
            "Title": book_title,
            "Price": book_price,
            "Availability": availability
        })

# Save the books data into a CSV file
df_books = pd.DataFrame(books_data)
df_books.to_csv('books_data.csv', index=False)
print("Book data saved to 'books_data.csv'.
")

print("Scraping completed successfully!")