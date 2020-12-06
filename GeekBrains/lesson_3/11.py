# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3
def calk(fraction_one_numerator, fraction_one_denominator, znak, fraction_two_numerator, fraction_two_denominator):
    common_denominator = int(fraction_one_denominator) * int(fraction_two_denominator)
    if znak == 'plus':
        result = int(fraction_one_numerator) * (int(common_denominator) / int(fraction_one_denominator)) + int(
            fraction_two_numerator) * (int(common_denominator) / int(fraction_two_denominator))
    else:
        result = int(fraction_one_numerator) * (int(common_denominator) / int(fraction_one_denominator)) - int(
            fraction_two_numerator) * (int(common_denominator) / int(fraction_two_denominator))
    return f'{int(result) // int(common_denominator)} {int(result) % int(common_denominator)}/{int(common_denominator)}'


def split_komponents(number):
    fraction_number_numerator = 0
    fraction_number_denominator = 0
    try:
        whole_number, fraction_number = str(number).strip().split(' ')
    except:
        if '/' in str(number):
            whole_number = '0'
            fraction_number_numerator, fraction_number_denominator = str(number).split('/')
        else:
            fraction_number_numerator, fraction_number_denominator = '1', '1'
            whole_number = number
    if int(whole_number):
        fraction_number_numerator = int(whole_number) * int(fraction_number_numerator)
    return fraction_number_numerator, fraction_number_denominator


def simple_fraction(fraction):
    if '+' in str(fraction):
        znak = 'plus'
        one, two = str(fraction).split(' + ')
    else:
        znak = 'minus'
        one, two = str(fraction).split(' - ')
    fraction_one_numerator, fraction_one_denominator = split_komponents(one)
    fraction_two_numerator, fraction_two_denominator = split_komponents(two)
    return calk(fraction_one_numerator, fraction_one_denominator, znak, fraction_two_numerator,
                fraction_two_denominator)


for el in [('5/6 + 4/7'), str('-2/3 - -2')]:
    print(simple_fraction(el))
