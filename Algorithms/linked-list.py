class Node: 
    def __init__(self, data=None) -> None:
        self.data = data
        self.nextNode = None
        
class LinkedList:
    def __init__(self) -> None:
        self.headNode = None
    def printList(self):
        printNode = self.headNode
        while printNode is not None:
            print(printNode.data)
            printNode = printNode.nextNode
            
l1 = LinkedList()
l1.headNode = Node("first node")
n2 = Node("second node")
n3 = Node("third node")

l1.headNode.nextNode = n2
n2.nextNode = n3

l1.printList()