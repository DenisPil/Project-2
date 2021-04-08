from pathlib import Path

URL = "https://books.toscrape.com/"

URL_CATEGORY = "https://books.toscrape.com/catalogue/"

CATEGORY = "https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html"

FIELDNAMES = [
                'product_page_url', 'universal_product_code',
                'title', 'price_including_tax', 'price_excluding_tax',
                'number_available', 'product_description', 'category',
                'review_rating', 'image_url'
             ]

DIRECTORY = Path.cwd() / 'book_to_scrap'
