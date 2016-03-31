from lxml import etree
import re
import pymysql
import pymysql.cursors

pattern = re.compile(r'^[А-Яа-яA-Za-z ]*$')
conn = pymysql.connect(host='', user='', password='', db='', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

with conn.cursor() as cursor:
    cursor.execute('SET NAMES utf8;')
    cursor.execute('SET CHARACTER SET utf8;')
    cursor.execute('SET character_set_connection=utf8;')
    while True:
        try:
            xml = etree.parse('http://export.yandex.ru/last/last20x.xml')
            nodes = xml.xpath('/page/last20x/item')
            for line in nodes:
                if pattern.match(line.text):
                    cursor.execute('INSERT INTO result (line, count, first_time) VALUES("%s", 1, NOW()) ON DUPLICATE KEY UPDATE count=count+1, last_time=NOW()' % line.text.lower())
                    print(line.text.lower())
        except Exception as e:
            print(e)
            pass
