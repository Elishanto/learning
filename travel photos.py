import requests
import re
import csv

blog_url = 'besttravelphotos.tumblr.com'


def request(method, data={}):
    url = 'http://api.tumblr.com/v2/blog/' + blog_url + '/' + method + '?api_key=eDd1s0TEK2W7Gn7seJfHU476QRwufxWuMdlp0wKGrQosIwMP6e&' + '&'.join(
            [x + '=' + str(data[x]) for x in data])
    data = requests.get(url).json()
    return data['response']


def strip_html(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data).strip()

get_caption = True

with open('photos.csv', 'w+', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Caption', 'URL'])
    count = request('info', {'filter': 'text'})['blog']['posts']
    for i in range(count // 20):
        for post in request('posts', {'offset': i * 20})['posts']:
            if 'photos' in post and 'url' in post['photos'][0]['original_size']:
                if get_caption:
                    writer.writerow([strip_html(post['caption']), post['photos'][0]['original_size']['url']])
                else:
                    writer.writerow(post['photos'][0]['original_size']['url'])
        print('{0:.1f}%'.format(i / (count // 20) * 100))
    print('{0:.1f}%'.format(100))
