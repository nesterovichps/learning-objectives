# Задача-1: поработайте с переменными, создайте несколько,
# выведите на экран, запросите от пользователя и сохраните в переменную, выведите на экран

integer_variable = 1
float_variable = 1.0
string_variable = '1'
bool_variable = True
list_variable = [1, 2, 3]
tuple_variable = (1, 2, 3)
dict_variable = {'1': 1, '2': 2, '3': 3}
set_variable = {1, 2, 3}
input_variable = input('Input text')

result = [
    integer_variable,
    float_variable,
    string_variable,
    bool_variable,
    list_variable,
    tuple_variable,
    dict_variable,
    set_variable,
    input_variable,
]
print(*[(f'variable = {i}, type variable = {type(i)}.') for i in result], sep='\n')
