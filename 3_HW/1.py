

import random


def create_list(length_of_list):
    l = []
    for i in range(length_of_list):
        l.append(random.randint(0, 10))
    return l

def find_sum(l):
    res = 0
    for i in range(len(l)):
        if not (i % 2 == 0):
            res = res + l[i]
    return res

n = int(input())
l = []
l = create_list(n)
print(l)
print(find_sum(l))

