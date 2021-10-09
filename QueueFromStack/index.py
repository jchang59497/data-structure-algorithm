class Queue: 
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()  
    def insert(self, value):
        self.stack1.insert(value)
    def remove(self):
        while(len(self.stack1.data) > 0):
            self.stack2.insert(self.stack1.remove())
        return self.stack2.remove()
        while(len(self.stack2.data) > 0):
            self.stack1.insert(self.stack2.remove())
