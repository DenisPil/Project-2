from def6_send_urls_books_to_find_info_books import send_urls_books_to_find_info_books
from def9_append_csv import append_csv


def save_info_in_csv():
    category = send_urls_books_to_find_info_books()

    for elem in category:

        append_csv(elem)

    return(elem)


if __name__ == '__main__':
    save_info_in_csv()
