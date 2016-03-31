import requests
from bs4 import BeautifulSoup
import csv


def is_rails(url):
    return len(
            BeautifulSoup(requests.get(url).content, 'html.parser').find_all('meta', attrs={'name': 'csrf-param'})) > 0

with open('result.txt', 'w+') as f:
    reader = list(csv.reader(open('top-1m.csv'), delimiter=',', quotechar='|'))
    for row in reader:
        url = 'http://' + row[1]
        try:
            if is_rails(url):
                f.write(url)
                print('YES ' + url)
            else:
                print('NO ' + url)
        except Exception:
            pass
