from pickle import FALSE, TRUE

def check_input(n):
    for i in range(len(n)):
        if not (n[i].isdigit() or n[i] == '.' or n[i] == ','):
            return FALSE
    return TRUE

n = input()
res = 0
if check_input(n):   
    for i in range(len(n)):
        if (n[i].isdigit()):
           res += int(n[i])
    print(res)
else:
    print("Неккоректный ввод\n")
