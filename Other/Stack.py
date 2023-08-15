class MyStack:

    def __init__(self):
        self.array = []

    def push(self,item):
        self.array.append(item)
    
    def pop(self):
        poppend_item = self.array.pop()
        return poppend_item

    def peek(self):
        return self.__currend()
    
    def __currend(self):
        return self.array[self.count()-1]
    
    def count(self):
        return len(self.array)
    
    def __iter__(self):
        self.index = self.count()-1

    def __next__(self):
        if self.index < 0:
            raise StopIteration()
        result = self.array[self.index]
        self.index -= 1
        return result
    
x = MyStack()



