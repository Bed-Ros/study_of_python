import re

match = re.search(r'iii', 'piiig')
print(match, match.group())

match = re.search(r'еее', 'привееет')
print(match, match.group())

match = re.search(r'е', 'привееет')
print(match, match.group())

# . обозначает любой символ кроме символа перевода строки \n
match = re.search(r'..т', 'привееет')
print(match, match.group())

# \w обозначает любую букву, цифру или знак подчеркивания
match = re.search(r'\w\w\w', '@#$asdf%^&*')
print(match, match.group())

# \d соответствует любой цифре
match = re.search(r'\d\d\d', 'w123xyz')
print(match, match.group())


# повторения
match = re.search(r'\w{4}', '@#$asdf%^&*')
print(match, match.group())

match = re.search(r'i+', 'piiig')
print(match, match.group())

# е+ — одно или более е, так много, насколько это возможножно
match = re.search(r'е+', 'привееееет')
print(match, match.group())

# возвращает первое вхождение л+
match = re.search(r'л+', 'параллелограмм')
print(match, match.group())


# поиск 3 цифр, возможно разделенных пробелами
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
print(match, match.group())

match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')
print(match, match.group())

match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
print(match, match.group())


# ^ - означает начало строки, так что совпадений с таким шаблоном не будет:
match = re.search(r'^b\w+', 'foobar')
print(match)

# а без ^ все ок:
match = re.search(r'b\w+', 'foobar')
print(match, match.group()) # bar

# $ означает конец строки:
match = re.search(r'foo\d+$', 'foo1barfoo2')
print(match, match.group()) # foo2


# найдем строку email
s = 'письма лично на почту a.vavilov-home@gmail.com ношу'
match = re.search(r'\w+@\w+', s)
if match:
	print(match.group())

# Наборы символов
match = re.search(r'[\w+.-]+@[\w.-]+', s)
if match:
	print(match.group())

# Группировка
# Если поиск шаблона в тексте будет успешен, то match.group(1) будет 
# содержать текст, соответствующий содержимому 1-й скобки слева, 
# а match.group(2) содержать текст, соответствующий содержимому 2-й скобки. 
# match.group() по-прежнему будет содержать весь текст, как обычно.
match = re.search(r'([\w+.-]+)@([\w.-]+)', s)
if match:
	print(match.group(), match.group(0), match.group(1), match.group(2))



# findall
s = 'some text abc@xyz.com foo bar alice-in-chains@gmail.com, \
freddie@queen.co.uk and on and on and on'

emails = re.findall(r'[\w.-]+@[\w.-]+', s)
print(emails)

# извлекаем имя и домен отдельно
emails = re.findall(r'([\w.-]+)@([\w.-]+)', s)
print(emails)

# только домен
emails = re.findall(r'(?:[\w.-]+)@([\w.-]+)', s)
print(emails)

# замена
# Строка замены может включать '\1', '\2'. которые ссылаются на текст 
# из group(1), group(2) и так далее из исходного текста.
new_s = re.sub(r'([\w.-]+)@([\w.-]+)', r'\1@supermail.com', s)
print(news)


# чтение из файла
f = open('text.html', 'r')
table = re.findall(r'''
    <tr>\s*?
        <td>(.*?)</td>\s*?
        <td>(.*?)</td>\s*?
        <td>(.*?)</td>\s*?
    </tr>''', 
    f.read(), re.DOTALL | re.VERBOSE)
print(table)


# Компиляция регулярных выражений
# Пусть есть некий поисковый запрос
# Извлечь из него код и удалить из него проблеы и "-"
q = 'MR 335-035 Уплотнитель расширителя крыла'
code_chars = re.compile(r'[a-zA-Z0-9_ -]+')
if code_chars.match(q): 
    for code in code_chars.findall(q):
        print( re.sub(r'[- ]', '', code) )














