# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

first = input()
second = input()

if len(first) < len(second):
    temp = first
    first = second
    second = temp

length1 = len(first)
length2 = len(second)
res = 0

for i in range(length1 - length2+1): 
    if first[i] == second[0]:
        check = 0
        for j in range(length2):
            if first[i+j] == second[j]:
                check += 1
            if check == length2:
                res += 1
print(res)