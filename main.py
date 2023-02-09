import requests

urls = ('https://wttr.in/%20Череповец',
        'https://wttr.in/%20SVO',
        'https://wttr.in/%20Лондон')

params = {'lang': 'ru', 'm': '', 'n': '', '': '%3F', 'q': '', 'T': '', 'u': ''}

for url in urls:
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)
