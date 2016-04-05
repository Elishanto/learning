import requests, json, csv
from bs4 import BeautifulSoup
from answer import Answer
from question import Question

url = 'https://otvet.mail.ru/api/v2/question?ajax_id=0&qid={}&sort=1&n=20&p=0'
count = int(
    BeautifulSoup(requests.get('https://otvet.mail.ru/open/').content, 'html.parser').find('div',
                                                                                           class_='gray-l dotted item item_ava item_similiar').find_all(
        'a')[1]['href'].split('/')[2])
i = count - 1000000
j = 1

page = json.loads(requests.get(url.format(i)).text)
with open('answers.csv', 'w+', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Question ID', 'User ID', 'Question', 'Description', 'Answerer ID', 'Answer'])
    while j < 1000000:
        if 'error' not in page:
            title = page['qtext']
            try:
                desc = page['qcomment']
            except AttributeError:
                desc = ''
            question = Question(page['qid'], page['usrid'], title, desc)
            if 'answers' in page:
                for answer in page['answers']:
                    toAppend = Answer(answer['usrid'], answer['atext'])
                    question.answers.append(toAppend)
                    print(question)
                    writer.writerow([question.qid, question.uid, question.name.replace(';', ',').replace('\n', ' '),
                                     question.desc.replace(';', ',').replace('\n', ' '), toAppend.uid,
                                     toAppend.text.replace(';', ',').replace('\n', ' ')])
            print(j)
            j += 1
        i += 1
        page = json.loads(requests.get(url.format(i)).text)
