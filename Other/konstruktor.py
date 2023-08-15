class Model():
    def checkModel():
        return 'Model'


class Product():
    def checkProduct():
        return 'Product'
    def __init__(self) -> Model:
        self.checkModel = Model.checkModel()
        



class Check():
    def __init__(self) -> Product:
        return Product.ch
        pass
