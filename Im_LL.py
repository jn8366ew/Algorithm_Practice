class Link_L():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self, data=None):
        self.data = data

    def _data(self):
        return self.data

    def _next(self):
        return self.next


