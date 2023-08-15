import random
computer = random.choice('RSP')

while True:
    s = str(input('Выберите одну из них: \nR - камень \nS - ножницы \nP - бумага \n' ))
    if s==computer:
        print('Ничья')
    elif (computer =='R' and s =='S') or (computer =='S' and s =='P') or (computer=='P' and s =='R'):
        print('Вы проиграли')
    elif (computer =='P' and s =='S') or (computer=='R' and s =='P') or (computer =='S' and s =='R') :
        print('Вы выиграли')
    
    else:
        print('Некорректный ввод')
        continue
    test = str(input('Хотите продолжить ?\n y - Да \n n - Нет\n'))
    if test.lower() == 'n':
        break