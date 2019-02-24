#!/usr/bin/python3

import os
import re
import sys
import codecs
import urllib.request

""" Logpuzzle
На сервере лежит 9 изображений, являющихся частями одного изображения 
(фото дикой природы).

Дан лог файл веб-сервера, в котором среди прочих запросов содеражатся запросы
к этим изображениям. Нужно вытащить из файла url всех изображений и скачать их.
Затем создать файл index.html и собрать с его помощью все изображения в одну
картинку.

Вот что из себя представляет строка лога:
101.237.66.11 - - [05/Jun/2013:10:44:02 +0400] "GET /images/animals_07.jpg HTTP/1.1" 200 13632 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

Замечание: для создания html файла можно использовать самую простую разметку:
<html>
<body>
<img src="img0.jpg"><img src="img1.jpg">...
</body>
</html>

Подсказка: скачать файлы можно двумя способами:

1. Воспользоваться функцией, сохраняющей url по заданному пути file_name:
urllib.request.urlretrieve(url, file_name)

2. Скачать url и сохранить в файле:
import urllib.request
import shutil
...
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

"""


def read_urls(filename):
    """ 
    Возвращает список url изображений из данного лог файла,
    извлекая имя хоста из имени файла (apple-cat.ru_access.log). Вычищает
    дубликаты и возвращает список url, отсортированный по названию изображения.
    """
    site_url = re.findall('(.*)_access\\.log', filename)
    site_url = 'http://' + site_url[0]
    f = codecs.open(filename, encoding='utf-8')
    text = f.read()
    dir_imgs = re.findall('.* (.*animals.*jpg).*\n', text)
    for i in range(len(dir_imgs)):
        dir_imgs[i] = site_url + dir_imgs[i]
    dir_imgs = list(set(dir_imgs))
    return sorted(dir_imgs)
  

def download_images(img_urls, dest_dir):
    """
    Получает уже отсортированный спискок url, скачивает каждое изображение
    в директорию dest_dir. Переименовывает изображения в img0.jpg, img1.jpg и тд.
    Создает файл index.html в заданной директории с тегами img, чтобы 
    отобразить картинку в сборе. Создает директорию, если это необходимо.
    """
    f = open(dest_dir + '/index.html', 'tw', encoding='utf-8')
    lines = ['<html>\n', '<body>\n']
    for i in range(len(img_urls)):
        file_name = dest_dir + '/img' + str(i) + '.jpg'
        urllib.request.urlretrieve(img_urls[i], file_name)
        lines.append('<img src="img' + str(i) + '.jpg">')
    lines.extend(['\n', '<body>\n', '<html>\n'])
    f.writelines(lines)


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        for n in img_urls:
            print('\n'.join(n))

if __name__ == '__main__':
    main()
