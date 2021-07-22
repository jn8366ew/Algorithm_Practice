from Stack import Stack

class SQLink(Stack):

    class Node:
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):
        self.size = 0
        self.tail = None

    def push(self, ele):
        new_node = self.Node(ele, None)
        if self.is_empty():
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

        self.tail = new_node
        self.size += 1


    def is_empty(self):
        return self.size == 0

    # 첫번째 원소 삭제
    def pop(self):
        old_head = self.tail.next
        ele = old_head.data
        if self.size > 1:
            self.tail.next = old_head.next
            old_head = None
        else:
            self.tail = None

        self.size -= 1
        return ele

    def top(self):
        return self.tail.next.data



s = SQLink()
s.push(1)

print(s.top())
print(s.is_empty())
s.push(2)

print(s.pop())
print(s.top())
print(s.pop())
print(s.is_empty())
