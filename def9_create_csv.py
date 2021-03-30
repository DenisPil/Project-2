import csv


def create_csv(info):

    with open('category-' + info['category'] + '.csv', 'w',  encoding='utf-8-sig', newline='') as csvfile:
        fieldnames = ['product_page_url', 'universal_product_code',
                      'title', 'price_including_tax', 'price_excluding_tax',
                      'number_available', 'product_description', 'category',
                      'review_rating', 'image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for elem in info['books_info']:
            print(elem)
            writer.writerow(
                    {
                        'product_page_url': elem['product_page_url'],
                        'universal_product_code': elem['UPC'],
                        'title': elem['title'],
                        'price_including_tax': elem['Price_(incl._tax)'],
                        'price_excluding_tax': elem['Price_(excl._tax)'],
                        'number_available': elem['Availability'],
                        'product_description': elem['product_description'],
                        'category': elem['category'],
                        'review_rating': elem['review_rating'],
                        'image_url': elem['image_url']
                    }
                )


if __name__ == '__main__':
    create_csv(info="azeaze")
