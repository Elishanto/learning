import csv
from collections import Counter

phrases = {}
relations = {}
with open('bbt.csv') as f:
    reader = csv.reader(f, delimiter=';', quotechar='|')
    for row in reader:
        if row[2] not in ['Man', 'Mrs', 'Boys', 'All', 'Both', 'All together', 'Ra', 'Scene'] and not any(i.isdigit() for i in row[2]):
            if row[2] not in phrases:
                phrases[row[2]] = []
            phrases[row[2]].append(row[3])
for speaker, phrasesOfPerson in phrases.items():
    for person in phrases.keys():
        for phrase in phrasesOfPerson:
            if person in phrase:
                if speaker not in phrase:
                    if speaker not in relations:
                        relations[speaker] = []
                    relations[speaker].append(person)
relations = {x: Counter(y) for x, y in relations.items()}
with open('bbt_relations.csv', 'w+') as f:
    writer = csv.writer(f, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Source', 'Target', 'Type', 'Weight'])
    for person, relation in relations.items():
        for to, count in relation.items():
            writer.writerow([person, to, 'Undirected', count])