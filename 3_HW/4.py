# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def decimalToBinary(n, res):
    if n > 1:
        decimalToBinary(n//2, res)  
    #print(n%2, end=' ')
    res.append(n%2)

print('Enter number')
res = []
decimalToBinary(int(input()), res)
print(*res)
