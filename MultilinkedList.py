from Node import Node

class MultiLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, Node):
        node = Node
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            current = self.tail
            current.next = node
            node.prev = current
            self.tail = node
        return node
    
    def print_multilist(self, level=0):
        if self.head is None:
            print("Empty List")
            return
        current = self.head
        while current:
            print(" "+level+ str(current))
            if current.subList:
                current.subList.print_multilist(self, level+1)
            current= current.next
    
    def addChild(self, parent, child):
        if parent.subList is None: 
            subList = MultiLinkedList()
            subList.head = child
            subList.tail = child
            parent.subList = subList
        else:
            current = parent.subList.tail
            current.next = child
            child.prev = current
            parent.subList.tail = child
        return parent.subList