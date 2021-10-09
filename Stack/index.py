class Stack:
    def __init__(self):
        self.data = []
    def insert(self,value):
        self.data.append(value)
    def remove(self):
        return self.data.pop()
    def last(self):
        if len(self.data) == 0:
            print('Array is empty')
        return self.data[len(self.data)-1]
