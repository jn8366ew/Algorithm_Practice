class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        self.head = None
        self.tail = None

class ll:
    def __init__(self):
        head = None


a = ll()

b = Node(2)
c = Node(3)


ll.head = Node(1)
ll.head.next = b
b.next = c


