class Node:
    
    def __init__(self, attribute, data):
        self.data=data
        self.attribute = attribute
        self.next = None
        self.prev = None
        self.subList = None