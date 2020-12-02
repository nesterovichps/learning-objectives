# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
list_one = [1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9]
list_two = [1, 1, 10, 10, 3, 3, 11, 20, 5, 12, 7, 13, 9, 14]
temp_list = []
for element in list_one:
    if element not in list_two:
        temp_list.append(element)
list_one.clear()
list_one = temp_list.copy()
print(list_one)
