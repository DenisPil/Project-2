--> INDEX
-----> LIST CATEGORIES (première page) ... get_categories
-----> LIST CATEGORIES (toutes les pages)... find_all_pages_for_one_category

for cat in get_categories
    find_all_pages_for_one_category --> liste de URLs
{ "cat_name": "Voyage"
  "cat_urls": ["voyage-1.html", voyage-2.html]

---> 1 CATEGORY AVEC TOUTES LES PAGES
----> liste de toutes les URLs des books.... get_books_url_from_one_category_dict
def ....(cat_dict)
for url in cat_dict["cat_urls"]:
    get_books_url_from_one_category_url

for book_url in ...
    get_book_information(book_url)

----> dictionnaires



url_categories = get_categories_urls()


url_books = list()

[
    {
        "cat_url"
        "cat_name":
        "books": [
            {
                "price":
                "name":
                "book url":
            }
    }
]

for url_cat in url_categories:
    books.append(get_cat_info(url_cat))

for url_book in url_books:
    dico = get_book_info(url_book)
    list_book_dico.append(dico)

for category in list_categories:
   save_csv(category)

def save_csv(category):
    open(category.name.csv)
    csv.DictWriter(...)
    for book in category["books"]:
        csv.writerow(book)
