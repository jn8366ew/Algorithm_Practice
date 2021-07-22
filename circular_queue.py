class circular_queue:

    def __init__(self, k:int):
        self.q = [] * k
        self.max_len = k
        self.front = 0
        self.rear = 0

    def enqueue(self, e):
        if self.q[self.rear] is None:
            self.q[self.rear] = e
            self.rear = (self.rear + 1) % self.max_len
            return True

        else:
            return False

    def dequeue(self):
        if self.q[self.front] is None:
            return False

        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.max_len
            return True

    def first(self):
        return self.q[self.front] if self.q[self.front] else False

    def last(self):
        return self.q[self.rear-1] if self.q[self.rear-1] else False

    def is_empty(self):
        return self.front == self.rear and self.q[self.front] is None

    def is_full(self):
        return self.front == self.rear and self.q[self.front] is not None








