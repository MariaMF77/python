# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1



def fibonacci(n, m):
    i = 0
    fb_lst = []
    while i <= m-1:
        if i == 0:
            fb_lst.append(1)
        elif i == 1:
            fb_lst.append(1)
        else:
            fb_lst.append(fb_lst[i-2] + fb_lst[i-1])
        i += 1
    return fb_lst[n-1:]
    
print('# Задача-1')
n = int(input('Введите n '))
m = int(input('Введите m '))
print(fibonacci(n, m))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = len(origin_list)
    for l in range(0, n - 1):
        is_sorted = 0
        for i in range(0, n - l - 1):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
                #print(origin_list[i], origin_list[j])
                is_sorted = 1
        if is_sorted == 0:
            break
    return(origin_list)

print('# Задача-2')
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(arg, data):
    result = []
    a = list(map(arg, data))
    for ind, val in enumerate(a):
        if val == True:
            result.append(data[ind])
    return result

print('# Задача-3')
data = [-2, -10, 5, 19]
# Отфильтруем, выбрав из списка только четные числа
print(my_filter(lambda x: x // 2 == x / 2, data))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def is_prlg(c1, c2, c3, c4):
    # по всем точкам проверяем, есть ли сочетание, для которого выполняется условие параллелограмма
    #    x1 + x3 ≈ x2 + x4
    #    y1 + y3 ≈ y2 + y4
    if (c1[0] + c2[0] == c3[0] + c4[0]) and (c1[1] + c2[1] == c3[1] + c4[1]) or \
            (c1[0] + c3[0] == c2[0] + c4[0]) and (c1[1] + c3[1] == c2[1] + c4[1]) or \
            (c1[0] + c4[0] == c2[0] + c3[0]) and (c1[1] + c4[1] == c2[1] + c3[1]):
        res = 'Это параллелограм!'
    else:
        res = 'Это не параллелограм, а что-то другое!'
    return res

print('# Задача-4')
#Задаем координаты
A1 = (1, 1)
A2 = (3, 2)
A3 = (3, 4)
A4 = (1, 3)

print(is_prlg(A1, A2, A3, A4))
