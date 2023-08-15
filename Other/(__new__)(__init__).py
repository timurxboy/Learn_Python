 class Character():
    __instance = None

    def __new__(cls):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.race = 'Elf'

c = Character()
print(c.race)

d = Character()
d.race = 'Ork'
print(c.race)
print(d.race)
