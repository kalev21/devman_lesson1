import requests

url_1 = 'https://wttr.in/%20Череповец?m?n?qTqu&lang=ru'
url_2 = 'https://wttr.in/%20SVO?m?n?qTqu&lang=ru'
url_3 = 'https://wttr.in/%20Лондон?m?n?qTqu&lang=ru'
response_1 = requests.get(url_1)
response_2 = requests.get(url_2)
response_3 = requests.get(url_3)
response_1.raise_for_status()
print(response_1.text)
print(response_2.text)
print(response_3.text)
