import requests
from bs4 import BeautifulSoup
import csv

page = BeautifulSoup(requests.get('https://bigbangtrans.wordpress.com/').content, 'html.parser')
transcripts = []
with open('bbt.csv', 'w+', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Series', 'Episode', 'Character', 'Phrase'])
    for episode in page.find('div', class_='widget_pages').find_all('li')[1:]:
        for phrase in BeautifulSoup(requests.get(episode.find('a')['href']).content, 'html.parser').find('div', class_='entrytext').find_all('p'):
            if ':' in phrase.text:
                writer.writerow([episode.text.split()[1], episode.text.split()[3], phrase.text.split(':')[0].split('(')[0].strip(), ':'.join(phrase.text.split(':')[1:]).replace('\n', ' ')])
        print(episode.text)