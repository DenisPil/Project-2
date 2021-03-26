from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
from constants import URL


def scrap_info_table(urlX='une url'):

    url = urlX
    prod_info = []
    for i in url:
        print(i)
        continue
        response = requests.get(i)
        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('h1').text
        product_description = soup.findAll('p')[3].text.replace('\n', '')
        review_rating = soup.find('p', class_='star-rating')['class'][1]
        category = soup.find('ul', {'class': 'breadcrumb'}).findAll('li')[2].text.replace('\n', '')
        image_url_no_join = soup.find('img', src_='')['src']
        image_url = urljoin(URL, image_url_no_join)
        info_dico = {
            'product_page_url': i,
            'title': title,
            'product_description': product_description,
            'category': category,
            'review_rating': review_rating,
            'image_url': image_url
            }

        product_information = soup.find('table', {'class': 'table table-striped'}).findAll('tr')
        dict_prod_information = process_tr(product_information)
        info_dico.update(dict_prod_information)
        prod_info.append(info_dico)

    return(prod_info)

def process_tr(product_information):
    info_dico = dict()
    for prod in product_information:
        th = prod.find('th').text.replace(' ', ('_'))
        td = prod.find('td').text.replace('In stock', '')
        if td == '':
            td = ('no info')
        one_info = {th: td}
        info_dico.update(one_info)
    return info_dico


if __name__ == '__main__':
    scrap_info_table(urlX='une url')
