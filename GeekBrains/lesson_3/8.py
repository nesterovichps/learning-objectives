# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    len_list=len(origin_list)
    i=0
    sort=['bad']
    while 'bad' in sort:
        if i+1==len_list:
            i=0
            sort.clear()
            for num_1,num_2 in (zip(origin_list[:-1],origin_list[1:])):
                if num_1<=num_2:
                    sort.append('good')
                else:
                    sort.append('bad')
            continue
        el1,el2=origin_list[i],origin_list[i+1]
        if el1>el2:
            origin_list[i], origin_list[i+1] = el2,el1
        i+=1
    return origin_list

sort_list=[2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print(sort_list)
print(sort_to_max(sort_list))
