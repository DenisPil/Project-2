import os
from urls import urls_cat
from urls import pages_category
from urls import urls_books
from books import info_book
from directory_and_file import create_csv
from directory_and_file import save_images
from directory_and_file import create_directory


def main():

    get_url_cat = urls_cat()
    directory = create_directory()
    os.chdir(directory)
    # Création boucle qui prend les ulrs des catégories.
    for elem in get_url_cat:
        url_cat = (elem['url_category'])
        name_category = (elem['name_category'])

        find_urls_pages = pages_category(url_cat)

        find_urls_books = urls_books(find_urls_pages)

        get_info_book = info_book(find_urls_books)

        save_info = create_csv(name_category, get_info_book)

        save_image = save_images(get_info_book)

    return 0


main()
