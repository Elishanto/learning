import re

regex = re.compile(r'[А-Яа-яA-Za-z\d]')
with open('hashtag.out', 'w+', encoding='utf-8') as fout:
    with open('hashtag.in', encoding='utf-8') as fin:
        for line in fin:
            fout.write(' '.join('#' + word if regex.match(word) else word for word in line.split()).strip() + '\n')
