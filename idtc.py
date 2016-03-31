import requests
from bs4 import BeautifulSoup

locations = BeautifulSoup(requests.get('https://www.idtech.com/locations/').content, 'html.parser').find('div',
                                                                                                         class_='row has_alts')

camps = []
for row in locations.find_all('div', class_='col-md-4'):
    for state in row.find(class_='states').find_all(class_='state'):
        for host in [x for x in state.find(class_='host-location-container').find_all(class_='host-location') if
                     'idtc' in x['class'] and x.find('span', class_='division25') is not None]:
            camp = BeautifulSoup(requests.get(host.find('a')['href']).content, 'html.parser')
            src = camp.find(id='content_frame')['src'].split('redirect=https%3A%2F%2F')[1]
            frame = BeautifulSoup(requests.get(src).content, 'html.parser')
            prices = BeautifulSoup(requests.post(src, data={
                '__VIEWSTATE': frame.find(id='__VIEWSTATE')['value'],
                '__VIEWSTATEGENERATOR': frame.find(id='__VIEWSTATEGENERATOR')['value']
            }).content, 'html.parser')
            print(prices)
            camps.append({'name': host.find('a').text, 'state': state.find(class_='expand-state').text})
            print(camps)
