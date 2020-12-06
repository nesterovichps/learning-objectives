# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def where_to_round(digit):
    if digit < 5:
        el1, el2 = 0, 0
        return el1, el2
    el1, el2 = 1, 0
    return el1, el2


def my_round(number, ndigits):
    number = str(number)
    temp_number = []
    counter_num = list(range(int(ndigits + 1)))
    for i in counter_num:
        if number[i] == '.':
            counter_num.append(int(ndigits) + 1)
            temp_number.append('.')
            continue
        temp_number.append(number[i])
    temp_number.reverse()
    result_nuber = []

    el_1, el_2 = where_to_round(int(temp_number[0]) )

    for el in temp_number[1:]:
        if el == '.':
            result_nuber.append('.')
            continue

        if el_1:
            if el == '9':
                el_1, el_2 = where_to_round(int(el) + el_1)
                result_nuber.append(el_2)
            else:
                result_nuber.append(el_1+int(el))
                el_1=0

        else:
            result_nuber.append(int(el)+el_1)
    result_nuber.reverse()
    result_nuber = result_nuber
    return ''.join(map(str,result_nuber))


print(2.1234567, 5)
print(my_round(2.1234567, 5))
print(2.1234467, 5)
print(my_round(2.1234467, 5))

print(21234567, 5)
print(my_round(21234567, 5))

print(2.1999967, 5)
print(my_round(2.1999967, 5))

print(2.9999967, 5)
print(my_round(2.9999967, 5))
