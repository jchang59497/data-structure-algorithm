class Node: 
    def __init__(self, data):
        self.data = data
        self.children = []
    
    def add(self, data):
        self.children.append(Node(data))

    def remove(self, data):
        for x in range(0, len(self.children)):
            if self.children[x].data == data:
                self.children = self.children[0:x] + self.children[x + 1:]
                return "You successfully removed " + data
        return 'The' + data + 'is not there.'
            
                
class Tree:
    def __init__(self, node)
        self.root = node
    
    def traverseDF():
        solution = []
        helper = [self.root]
        
        while (len(helper) > 0):
            currNode = helper.pop(0)
            helper = currNode.children + helper
            solution.append(currNode)
            
        return solution
    
    def traverseBF():
        solution = []
        helper = [self.root]
        
        while (len(helper) > 0):
            currNode = helper.pop(0)
            helper = helper + currNode.children
            solution.append(currNode)
            
        return solution