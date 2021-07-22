import collections

class Sq:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)
        for i in range(len(self.input)):
            print(self.input[i])

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
            print(self.output)
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []

    def pop(self):
        self.peek()
        return self.output.pop()



a = Sq()
a.push(1)
a.push(2)
a.push(3)
print(a.peek())
print(a.pop())
print(a.empty())