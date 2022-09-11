# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

from pickle import FALSE


def create_list(n):
    l = []
    for i in range(2*n):
        if (i % 2 == 0):
            l.append(-n+i)
    return l

def find_mult(l, a, b, error):
    if(abs(a) < len(l) and abs(b) < len(l)):
        res = l[a]*l[b]
    else:
        print('Неккоректно введены данные')
        error = 1
        res = 0
    return res

l = create_list(int(input()))
print(l)
error = 0
res = find_mult(l, int(input()), int(input()), error)
if not error: 
    print(res)
