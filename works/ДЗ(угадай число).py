import random
number = random.randint(1,50)
for i in range(1,7):
    input_number = int(input())
    if input_number==number:
        print('Вы угадали')
    elif input_number>number:
        print('Меньше')
    else:
        print('Больше')