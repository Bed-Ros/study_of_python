# Работа с файловой системой
# os, os.path, shutil

import os
import shutil


# листинг директорий
print(os.listdir())
print(os.listdir('/'))

# создание директории
os.mkdir('test')
print(os.listdir())
os.rmdir('test')


# созданим файл
open('test.txt', 'w')

# проверка существования файла
os.path.exists('test.txt')

# удаление файла
os.remove('test.txt')


# рекурсивное создание директорий
path = 'test/subtest/subsubtest'
# os.mkdir(path) # вызовет ошибку
os.makedirs(path)
# os.rmdir(path) # удалит только последнюю директорию subsubtest
shutil.rmtree('test') # удалит все дерево каталогов и файлов test


path = '/home/vasily/spam'
filename = 'eggs.html'
fullpath = os.path.join(path, filename)
print(fullpath)
print(os.path.dirname(fullpath))
print(os.path.basename(fullpath))


# Перебор файлов в директории
dir_ = 'exercises'
filenames = os.listdir(dir_)
for filename in filenames:
    print(filename) # имя файла
    print(os.path.join(dir_, filename)) # путь относительно текущей директории
    print(os.path.abspath(os.path.join(dir_, filename))) # абсолютный путь


# копируем файлы
os.mkdir('test1')
open('test1/text.txt', 'w+').write('text '*5)
os.mkdir('test2')
shutil.copy('test1/text.txt', 'test2/') # указываем только конечную директорию
shutil.copy('test1/text.txt', 'test2/text copy.txt') # копироние с переименованием
