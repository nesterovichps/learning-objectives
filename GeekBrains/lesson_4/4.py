# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки,
# имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
import re

refular_pattern_1 = '[А-ЯA-Z][a-zа-я]+'
refular_pattern_2 = '[a-z0-9_]+@[a-z]+\.(org|com|ru)'

f = 1
while f:
    first_name = input('enter first name ')
    if re.match(refular_pattern_1, first_name):
        f = 0
f = 1
while f:
    last_name = input('enter last name ')
    if re.match(refular_pattern_1, last_name):
        f = 0
f = 1
while f:
    email = input('enter email ')
    if re.match(refular_pattern_2, email):
        f = 0
print(f'hello {first_name} {last_name}, you email {email}')
