print("введите Х:")
x = int(input())
print("введите Y:")
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
elif x == 0 and y > 0:
    print("On the positive side of y-axis")
elif x == 0 and y < 0:
    print("On the negative side of y-axis")
elif x > 0 and y == 0:
    print("On the positive side of x-axis")
elif x < 0 and y == 0:
    print("On the negative side of x0-axis")
else:
    print("wrong input")