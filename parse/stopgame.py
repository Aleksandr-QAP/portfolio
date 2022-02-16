import requests
from bs4 import BeautifulSoup
import csv
import os

FILE = 'title.csv'

def get_html(url, params=None):
    r = requests.get(url, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('a', class_='item')
    if pagination:
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.select('.items > .article-summary')

    titles = []
    for item in items:
        titles.append({
            'title': item.find('div', class_='caption-bold').find('a').get_text(),
            'date': item.find('span', class_='timestamp').get_text(),
            'comment': item.find('a', class_='comments-link').get_text(strip=True)
        })
    return titles


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Статья', 'Дата публикации', 'Количество комментариев'])
        for item in items:
            writer.writerow([item['title'], item['date'], item['comment']])


def parse():
    URL = input('Введите URL: ')
    URL = URL.strip()
    html = get_html(URL)
    if html.status_code == 200:
        titles = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'Парсинг страницы {page} из {pages_count}...')
            html = get_html(URL, params={'page': page})
            titles.extend(get_content(html.text))
        save_file(titles, FILE)
        print(f'Получено {len(titles)} статей')
        os.startfile(FILE)
    else:
        print('Error')


parse()
