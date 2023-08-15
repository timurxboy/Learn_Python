def get_number():
    while True:
        try:
            reply = int(input('Введите число ...\n'))
            return reply
        # except:
        #     print('Некорректный ввод!')
        #     break    
        #     print(123)
        finally:
            print(456)

print(get_number())