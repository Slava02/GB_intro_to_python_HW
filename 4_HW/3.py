from random import randint

def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers
            
numbers = []
for i in range(20):
    numbers.append(randint(-10, 10))

print(numbers)

print(get_unique_numbers(numbers))



