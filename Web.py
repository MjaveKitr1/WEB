import requests
from bs4 import BeautifulSoup
import csv
import time

url = 'https://theuselessweb.com'

def get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_info(soup):
    info = soup.find_all('div', class_='BNeawe iBp4i AP7Wnd')
    return info

def write_to_csv(info):
    with open('info.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['info'])
        for i in info:
            csv_writer.writerow([i.text])

def main():
    soup = get_page(url)
    info = get_info(soup)
    write_to_csv(info)
    time.sleep(15)

if __name__ == '__main__':
    main()