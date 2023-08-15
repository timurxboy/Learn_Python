class Peoples():
    def __init__(self) -> None:
        print('Создан класс People')

    def name(self):
        raise NotImplementedError('Тимур')

    def surname(self):
        print('Рахимкулиев')

    def age(self):
        print('22')
    
class Student(Peoples):
    def __init__(self) -> None:
        Peoples.__init__(self)

    def group(self):
        group_number = 944
        return group_number
    
    def age():
        print('30')

x = Student()
print(x.name)
