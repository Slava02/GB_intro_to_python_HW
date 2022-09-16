import random

def create_list(length, min, max):
    return[random.randint(min, max) for i in range(length)]

def find_mult_of_pairs(l):
    res = []
    len_of_list = len(l)
    res = [l[i] * l[-i - 1] for i in range(int(len_of_list/2))]
    if not (len(l) % 2 == 0):
      res.append(l[int(len_of_list/2 + 1)]**2)
    return res

length = int(input())
min = int(input())
max = int(input())

my_list = create_list(length, min, max)
print(my_list)
print(find_mult_of_pairs(my_list))