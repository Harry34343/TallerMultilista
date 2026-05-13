from Node import Node

class MultiLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self, attribute, data):
        node = Node(attribute, data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            current = self.tail
            current.next = node
            node.prev = current
            self.tail = node
        return node
    
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
    
    def csvToLinkedList(self, csvName):
        with open(csvName, mode="r", encoding="utf-8") as f:
            todo = f.read()
        header = todo[0]
        titles = header.split(",")
        code=5
        for line in todo[1:]:
            data = line.split(",")
            parent = self.head
            if data[0] != code:
                parent = parent.next
            if parent is None:
                parent = self.addNode(data[1], data[0])
            parent.sublist = MultiLinkedList()
            code = data[0]
            node = Node(data[1], code)
            if self.head.subList is None:
                self.head.subList = MultiLinkedList()
                self.head.subList.head = node
                self.head.subList.tail = node
            else:
                current = self.head.subList.tail
                current.next = node
                node.prev = current
                self.head.subList.tail = node