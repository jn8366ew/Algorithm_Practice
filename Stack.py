class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.last = None
        self.size = 0

    def push(self, data):
        self.last = Node(data, self.last)
        self.size += 1

    def pop(self):
        data = self.last.data
        self.last = self.last.next
        self.size -= 1
        return data

    def __len__(self):
        return self.size

    def valid(self, check_str):
        table = {
            ')': '(',
                 ']': '[',
                      '}': '{'
        }
        for char in check_str:
            if self.size == 0 or table[char] != self.pop():
                return False
        return True
