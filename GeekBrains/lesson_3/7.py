# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    result = []
    new_num = 1
    i = 0
    while True:
        i += 1
        if i < 3:
            old_num = new_num
        else:
            fib = old_num + new_num
            old_num = new_num
            new_num = fib
            if i >= n:
                result.append(old_num)
                if i == m + 1:
                    return result


n = 5
m = 20
print(*fibonacci(n, m), sep=', ')
