from def4_send_urls_pages_to_find_urls_books import send_urls_pages_to_find_urls_books
from def7_get_info_for_one_book import get_info_book


def send_urls_books_to_find_info_books():

    dict_all_info = {}
    list_all_info = []
    urls_books = send_urls_pages_to_find_urls_books()

    for elem in urls_books:

        url_book = (elem['url_book'])
        name_cat = (elem['name_category'])
        for elemA in url_book:
            get_info_book(elemA)

            dict_all_info = {'category': name_cat, 'books_info': get_info_book(elemA)}
            list_all_info.append(dict_all_info)

    # print(list_all_info)
    return(list_all_info)


if __name__ == '__main__':
    send_urls_books_to_find_info_books()
