import urllib.request
import urllib.parse
import re

# Откроем url и выведем в консоль
ufile = urllib.request.urlopen('http://yandex.ru')
html = ufile.read()
# если сайт в кодировке windows-1251 - используйте .decode('cp1251')
print(html.decode('utf-8')) 
print(ufile.info()) # метаинфомация о странице
print(ufile.geturl()) 
print(ufile.getcode()) # код ответа сервера


# # Запросим страницу через объект Request
# # и добавим заголовки
req = urllib.request.Request('http://www.yandex.ru')
req.add_header('Referer', 'http://www.python.org/')
req.add_header('User-agent', 'Mozilla/5.0')
print(req.headers)
f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))

# Преобразуем строку параметров в URL запрос
params = urllib.parse.urlencode({
    'redirect': 'http://abc.com', 
    'text': 'Привет, мир!'
})
print (params)


# # Отправка GET запросов
params = urllib.parse.urlencode({'text': 'python'})
f = urllib.request.urlopen("http://prog-school.ru/search/topics/?q=python%s" % params)
html = f.read().decode('utf-8')
# удалим теги
html = re.sub(r'<script.*?>.*?</script>', ' ', html, flags=re.DOTALL) 
html = re.sub(r'<.*?>', '', html) 
html = re.sub(r'\s+', ' ', html) 
print((html))


# POST запросы с помощью объекта класса Request
data = urllib.parse.urlencode({'text': 'iphone'})
data = data.encode('utf-8')
req = urllib.request.Request('http://market.yandex.ru/search.xml')
req.add_header('User-agent', 'Mozilla/5.0')
req.method = 'POST' # метод ставиновится POST
req.data = data # method становится POST автоматически, если задать data
print (req.get_method())

f = urllib.request.urlopen(req)
html = f.read().decode('utf-8')
html = re.sub(r'<.*?>', ' ', html)
print(html)


# с помощью urllib.parse можно делать разбор URL
from urllib.parse import urlparse
url = 'https://docs.djangoproject.com/en/1.5/intro/overview/#design-your-model'
print(urlparse(url))

url = 'https://docs.djangoproject.com/search/?q=admin&release=7'
print(urlparse(url))


# Скачиваем url и сохраняем файл по заданному пути file_name:
# urllib.request.urlretrieve(url, file_name)

# Скачать url и сохранить в файле:
# import urllib.request
# import shutil
# ...
# with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
#     shutil.copyfileobj(response, out_file)


