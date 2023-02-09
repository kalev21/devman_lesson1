import requests

url = 'https://wttr.in/san%20francisco?nTqu&lang=en'
response = requests.get(url)
response.raise_for_status()     # Обязательная строчка. Нужна для понимания получения отклика от сервера.
print(response.text)



# url_1 = 'https://vsegda-pomnim.com/uploads/posts/2022-04/1650516991_77-vsegda-pomnim-com-p-tsvetok-foto-80.jpg'
# response_1 = requests.get(url_1)
# response_1.raise_for_status()
#
# filename = 'pic.jpg'
# with open(filename, 'wb') as file:
#     file.write(response_1.content)
