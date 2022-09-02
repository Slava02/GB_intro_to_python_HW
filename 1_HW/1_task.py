day = int(input())
if day in range(1, 6):
    print('нет')
elif day in range(6, 8):
    print('да')
else:
    print('Wrong input')