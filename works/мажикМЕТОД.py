class Road():
    def __init__(self, lenght) -> None:
        self.lenght = lenght

    def __len__(self):
        return self.lenght

    def __str__(self) -> str:
        return f'A road of lenght:{self.lenght}'
    
    def __del__(seld):
        print(f'The road has been destroyed')

r = Road(100)
len(r)
print(r)
del r