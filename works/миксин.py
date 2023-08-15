class PrintableMixin:
    def print_info(self):
        print(f'Имя {self.name}')
        print(f'Возраст {self.age}')
class Person(PrintableMixin):
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age 


person = Person("Тимур Рахимкулиев", 22)
person.print_info()