class People():
    def __init__(self, name, surname) -> None:
        self.__name = name
        self.__surname = surname
        self._age = 20
        
    
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age<0:
            self._age = 0
        elif age > 100:
            self._age = 100
        else:
            self._age = age 

p = People('Timur','Rakhimquliev')
p.age = 50
print(p.age)
print(p.name)
print()
print()