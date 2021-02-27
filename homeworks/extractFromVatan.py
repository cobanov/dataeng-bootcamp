# Author: Çağrı Köz
# Date: 13.02.2021

from bs4 import BeautifulSoup
import requests
import re
import csv
import logging
import time

logging.basicConfig(format='%(asctime)s - %(levelname)s [%(filename)s:%(lineno)d] - %(funcName)s - %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='extractFromVatanLogs.txt')

logger = logging.getLogger('scraping')


class Phones:
    def __init__(self):
        self.path = "https://www.vatanbilgisayar.com/cep-telefonu-modelleri/?page="

    def get_source(self, link):
        page = requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

    def get_page(self, link):
        soup = self.get_source(link)
        get_icon = soup.find_all('span', attrs={'class': 'icon-angle-right'})
        return get_icon

    def get_number(self, mix):
        fix = re.findall('[0-9]+', mix)[0]
        return fix

    def get_data(self, info: tuple, data: list):
        if info not in data:
            data.append(info)
        return data

    def get_info(self, link):
        data = []
        logger.info(f'Requesting {link}')
        soup = self.get_source(link)
        for page in soup.find_all('div', attrs={'class': 'product-list__content'}):
            name = page.select_one(
                'div.product-list__product-name').string.strip('\n').strip('\n ')
            cost = page.select_one(
                'div.product-list__cost span.product-list__price').string
            currency = page.select_one(
                'div.product-list__cost span.product-list__currency').string.strip(' ')
            try:
                rate = page.select_one('div.wrapper-star div.rank-star span')
                rate = self.get_number(rate['style']) + '%'
            except:
                rate = None
            try:
                comment_count = page.find(
                    'a', attrs={'class': 'comment-count'}).text
                comment_count = self.get_number(comment_count)
            except:
                comment_count = None
            try:
                condition = page.find_all(
                    'span', attrs={'class': 'wrapper-condition__text'})[0].text
            except:
                condition = None
            if rate or comment_count or condition:
                info = (name, cost, currency, rate, comment_count, condition)
                data = self.get_data(info, data)
        return data

    def get_all_data(self):
        all_data = []
        i = 1
        while self.get_page(self.path + str(i)):
            data = self.get_info(self.path + str(i))
            for info in data:
                all_data = self.get_data(info, all_data)
            i += 1
        last_data = self.get_info(self.path + str(i))
        for info in last_data:
            all_data = self.get_data(info, all_data)
        return all_data

    def get_csv(self):
        with open('extractFromVatan.csv', 'w', encoding='utf-8', newline='') as file:
            result = csv.writer(file, delimiter='|')
            result.writerows(self.get_all_data())
        return result


def main():
    start = time.time()
    logger.info("Data extract has been started.")
    phones = Phones()
    phones.get_csv()
    logger.info("Data extract has been ended.")
    end = time.time()
    print(f"Performance: {end - start}")


if __name__ == "__main__":
    main()

import os 
import shutil

shutil.copy2()
import pandas as pd

pd.read_csv()