from bs4 import BeautifulSoup
import requests
import plotly.plotly as py
import plotly.graph_objs as go
from time import strptime
from datetime import datetime
import random

data = []
urls = []
curs = BeautifulSoup(requests.get('http://www.exchangerates.org.uk/Russian-Rouble-RUB-currency-table.html').content, 'lxml').find_all(class_='currencypage-mini')[1].find_all('tr')
for rate in curs:
    cur = '-'.join(rate.find_all('td')[1].text.replace(' ', '-').split('-')[::-1])
    urls.append('http://www.exchangerates.org.uk/{}-exchange-rate-history-full.html'.format(cur))

for url in urls:
    page = BeautifulSoup(requests.get(url).content, 'lxml')
    table = page.find(id='hd-maintable').find('table')
    rates = []
    for tr in table.find_all('tr')[2:-1]:
        tds = tr.find_all('td')
        rates.append((' '.join(tds[0].text.split()[1:]), tds[1].text.split('=')[1].split()[0]))
    name = '/'.join(page.title.text.split()[1:3])
    dates = [strptime(x[0], '%d %B %Y') for x in rates]
    r = lambda: random.randint(0, 255)
    data.append(go.Scatter(
        x=[datetime(year=x[0], month=x[1], day=x[2]) for x in dates],
        y=[x[1] for x in rates],
        name=name,
        line={
            'color': 'rgb(%02X,%02X,%02X)' % (r(), r(), r())
        }
    ))
plot_url = py.plot(data, filename='full-rates')
