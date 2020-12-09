# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def func_filter(temp_func, temp_list):
    result = []
    for elem in temp_list:
        if bool(temp_func(elem)):
            result.append(elem)
    return result


if __name__ == '__main__':
    list_of_strings = ['one', 'two', 'list', '', 'dict', '100', '1', '50']
    list_of_words = ['one', 'two', 'list', '', 'dict']

    print(list(func_filter(str.isdigit, list_of_strings)))
    print(list(func_filter(lambda x: len(x) > 2, list_of_words)))
    print(list(func_filter(lambda x: x % 2, [10, 111, 102, 213, 314, 515])))
    print(list(func_filter(lambda x: not x % 2, [10, 111, 102, 213, 314, 515])))
