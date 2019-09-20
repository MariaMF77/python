# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    (a, b) = str(number).split('.')
    if len(b) > ndigits and ndigits > 0:
        # округление дробной части до нужного количества знаков
        a = int(a)
        if int(b[ndigits + 1]) > 5:
            b = int(b[:ndigits]) + 1
        else:
            b = int(b[:ndigits]) - 1

    result = a + b / (10 ** ndigits)
    return (result)

print('')
print('Задание-1')
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print('')

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    a = str(ticket_number)
    if len(a) != 6:
        return ('it isn\'s valid ticket number')
    if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]):
        return('it\'s a lucky ticket')
    else:
        return('it isn\'t lucky ticket')

print('')
print('Задание-2')
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print('')

