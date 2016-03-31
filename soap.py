import requests

url = 'http://javarush.ru/api/api1/JarCommonService'
headers = {'Content-Type': 'application/soap+xml; charset=utf-8;action=""'}
body = open('soap.xml').read()
response = requests.post(url, data=body, headers=headers)

print(response.content)