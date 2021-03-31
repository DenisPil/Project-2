import csv


def create_csv(file_name):

    csvfile = open(file_name, 'w',  encoding='utf-8-sig', newline='')
    fieldnames = ['product_page_url', 'universal_product_code',
                    'title', 'price_including_tax', 'price_excluding_tax',
                    'number_available', 'product_description', 'category',
                    'review_rating', 'image_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t') 
    writer.writeheader()
    csvfile.close()


if __name__ == '__main__':
    create_test(info['category']+'.csv')
