from db import query_user_last_seen, list_users
import time
from datetime import datetime, timedelta


def get_email_from_user(attempts=3, sleep_duration=10):
    # Пользователь вводит мейл, на ввод мейла у него 3 попытки, после чего пауза на 10 секунд.

    email = input("Введите e-mail: ")
    i = 1
    while (email.find("@") == -1):
        if i % attempts == 0:
            print("Переборщили с попытками. Подождите " + str(sleep_duration) + " секунд")
            time.sleep(sleep_duration)
        print("неправильный email. Попробуйте ещё раз")
        i = i + 1
        email = input("Попытка " + str(i) + ". Введите e-mail: ")

    return email


def make_username(email):
    # Мейл преобразуется в логин по правилу: все, что до символа собаки, — это
    # логин, а строка приводится к нижнему регистру.

    return email.split("@")[0].lower()


def check_user_date():
    # функция отвечает за информацию о том, когда пользователь с таким username последний раз заходил:

    existing_username = username
    last_seen = query_user_last_seen(existing_username)
    print("Пользователь", existing_username, "последний раз заходил", datetime.date(last_seen))
    return last_seen


def check_days_since_last_login():
    # Если с момента последнего введения логина прошло более 180 дней, вывести сообщение: «Вам надо подтвердить логин»

    if (datetime.now() - last_seen).days > 180:
        print('Вам надо подтвердить логин')
    # если меньше 180 дней, то вывести: «Ваш аккаунт подтвержден до...» и вместо
    # многоточия сегодняшняя дата + 180 дней.
    # Пример вывода: «Ваш аккаунт подтвержден до 2019-03-20».

    else:
        print('Ваш аккаунт подтвержден до', datetime.date(last_seen + timedelta(days=179)))


email = get_email_from_user()
username = make_username(email)
registered_users = list_users()
# Username проверяется по базе. Если в базе нет такого юзернейма,
# пользователю выводится строка «Вы с нами совсем недавно! Добро пожаловать».
if username not in str(registered_users):
    print("Вы вошли как " + username)
    print("Вы с нами совсем недавно! Добро пожаловать")
    print(str(registered_users))
else:
    # Если username в базе есть, то надо найти, когда пользователь логинился в последний раз.
    print("Вы вошли как " + username)
    last_seen = check_user_date()
    check_days_since_last_login()
