import os
import urls
import books
import directory_and_file


def main():

    get_url_cat = urls.search_category()
    directory = directory_and_file.create_directory()
    os.chdir(directory)
    # Création boucle qui prend les ulrs des catégories.
    for elem in get_url_cat:
        url_cat = elem['url_category']
        name_category = elem['name_category']

        find_urls_pages = urls.search_pages_category(url_cat)

        find_urls_books = urls.search_books(find_urls_pages)

        get_info_book = books.search_info(find_urls_books)

        directory_and_file.create_csv(name_category, get_info_book)

        directory_and_file.save_images(get_info_book)


main()
