# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх знаков после точки.
def power(n, p):
    res = n
    for i in range(p-1):
        res *= n 
    return res

def my_round(number, digits_after):
    x = power(10, digits_after)
    number = number * x
    if(number - int(number) >= 0.5):
        number = int(number) + 1
    else:
        number = int(number)
    s = str(number)
    l = list(s)
    l.insert(1, '.')
    return l


l = []
m = int(input())
sum = 0
for i in range(m):
    n = i+1
    x = power((1+1/n), n)
    l.append(x)
    sum = sum + x
for i in my_round(sum, 3):
    print(i, end = '')
print('\n')
