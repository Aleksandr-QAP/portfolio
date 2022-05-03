import random
from pathlib import Path


def password_gen(file_path='', serv='', login='', lop=''):

    if Path(file_path).is_file() and Path(file_path).suffix == '.txt':

        print(f'[+] Write file: {Path(file_path).name}')
        print('[+] Processing...')

        with open(file_path, 'a') as file:
            pas = ''
            for x in range(int(lop)):
                pas = pas + random.choice(list('!@#$%&1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
            file.write(serv + '  ' + login + '  ' + pas + '\n')
            file.close()

            return f'[+] {Path(file_path).name}.txt ready!'
    else:
        return 'File not exists, check the file path!'


def main():
    file_path = input('\nУкажите путь к файлу')
    serv = input('Сервис ')
    login = input('Логин ')
    lop = input('Длина пароля ')
    print(password_gen(file_path=file_path, serv=serv, login=login, lop=lop))


if __name__ == '__main__':
    main()
