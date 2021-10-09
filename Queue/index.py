class Queue:
    def __init__(self):
        self.data = []
         
    def insert(self,value):
        self.data.append(value)
        
    def remove(self):
        self.data.pop(0)
    
    def last(self):
        return self.data[len(self.data) - 1]
    
    def first(self):
        return self.data[0]
    
    def middle(self):
        return self.data[len(self.data) // 2]
