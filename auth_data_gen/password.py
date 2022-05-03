import random

f = open('test.txt', 'a')
serv = input('Сервис ')
login = input('Логин ')
lop = input('Длина пароля ')
try:
    pas = ''
    for x in range(int(lop)):
        pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    f.write(serv + '  ' + login + '  ' + pas + '\n')
finally:
    f.close()
