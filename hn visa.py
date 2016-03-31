import requests
from bs4 import BeautifulSoup
import csv

url = 'https://news.ycombinator.com/item?id=11012044'
page = BeautifulSoup(requests.get(url).content, 'html.parser')
jobs = input("Enter job list: ").split()
not_jobs = input("Enter exclude list: ").split()
visa = input("VISA/H1B (y/n): ")
if visa == 'y':
    visa = True
else:
    visa = False
with open('hn.csv', 'w+', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    if not_jobs and jobs:
        writer.writerow(['Job query', 'Not job', 'Offer'])
    elif not not_jobs and jobs:
        writer.writerow(['Job query', 'Offer'])
    elif not_jobs and not jobs:
        writer.writerow(['Not job', 'Offer'])
    else:
        writer.writerow(['Offer'])
    for comment in page.find('table', class_='comment-tree').find_all('tr'):
        offer = comment.find(class_='comment').text.strip().replace('\nreply', '').replace('\n', ' ').replace(';', ',')
        if visa:
            occurs = [job for job in jobs if
                      job.lower() in offer.lower() and ('visa' or 'h1-b' or 'h1b') in offer.lower()]
        else:
            occurs = [job for job in jobs if job.lower() in offer.lower()]
        not_occurs = [not_job for not_job in not_jobs if not_job.lower() in offer.lower()]
        if occurs and not not_occurs:
            if not_jobs and jobs:
                writer.writerow([', '.join(jobs), ', '.join(not_jobs), offer.strip()])
            elif not not_jobs and jobs:
                writer.writerow([', '.join(jobs), offer.strip()])
            elif not_jobs and not jobs:
                writer.writerow([', '.join(not_jobs), offer.strip()])
        elif not jobs and not not_jobs:
            writer.writerow([offer.strip()])

lines = open('hn.csv', 'r', encoding='utf-8').readlines()

lines_set = set(lines[1:])

out = open('hn.csv', 'w', encoding='utf-8')

out.write(lines[0])
for line in lines_set:
    out.write(line)
