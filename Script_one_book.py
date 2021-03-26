from def_scrap_info_table import scrap_info_table
from def_save_info import save_info


def scrap_one_book():
    urlX = scrap_info_table('https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html')

    return urlX


def save_csv():
    name_and_source = save_info("book-A-Light-in-the-Attic.csv", scrap_one_book())


if __name__ == '__main__':
    scrap_one_book()
    save_csv()
