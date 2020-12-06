# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if sum(map(int,str(ticket_number)[0:4]))==sum(map(int,str(ticket_number)[4:])):
        return 'lucky'
    return 'Not lucky'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
