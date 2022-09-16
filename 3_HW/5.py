# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(k):
    first_counter, second_counter = k - 2, k - 2
    fb_1, fb_2 = 1, 1
    neg_fb_1, neg_fb_2 = 1, -1

    res_neg_fb = [1, -1]
    res_fb = []
   
    while first_counter > 0:
        neg_fb_dif = neg_fb_1 - neg_fb_2
        res_neg_fb.append(neg_fb_dif)
        neg_fb_1 = neg_fb_2
        neg_fb_2 = neg_fb_dif
        first_counter -= 1
    reversed_res = list(reversed(res_neg_fb))
    for i in range(len(reversed_res)):
        print(reversed_res[i],', ',end = '')
    
    print(0, end = ', ')

    print(fb_1,',',fb_2,end = ', ')
    while second_counter > 0:
        fb_sum = fb_1 + fb_2
        print(fb_sum, end = ', ')
        fb_1 = fb_2
        fb_2 = fb_sum
        second_counter -= 1

fib(int(input()))