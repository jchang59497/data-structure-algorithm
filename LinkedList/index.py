class Node: 
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertFirst(self, data):
        self.head = Node(data)
    
    def getFirst(self):
        return self.head
    
    def clear(self):
        self.head = None
    
    def size(self):
        count = 0
        currNode = self.head 
        
        while currNode != None:
            count += 1
            currNode = currNode.next
            
            if currNode == None:
                return count    
        return count
    
    def insertLast(self, data):
        if self.head == None:
            self.insertFirst(data)
            return
        currentNode = self.head
        for x in range(0, self.size() - 1):
            currentNode = currentNode.next
        currentNode.next = Node(data)
        
    def getLast(self):
        if self.head == None:
            return 'No Nodes in this list!'
        
        if self.head.next == None:
            return self.head
        currentNode = self.head
        for x in range(0, self.size() - 1):
            currentNode = currentNode.next
        return currentNode
    
    def getAt(self, data):
        if self.head == None:
            return 'No Nodes in this list'
        if data > self.size():
            return 'The number exceeds the size of the linked list'
        currentNode = self.head
        for x in range(0, data - 1):
            currentNode = currentNode.next
        return currentNode
    
    def insertAt(self, i, data):
        currentNode = self.head
        prevNode = None
        for x in range(0, i):
            prevNode = currentNode
            currentNode = currentNode.next
        
        currentNode = Node(data, prevNode.next)
        prevNode.next = currentNode
        
    def removeAt(self, data): 
        currentNode = self.head
        prevNode = None
        for x in range(0, data):
            prevNode = currentNode
            currentNode = currentNode.next
        prevNode.next = currentNode.next
