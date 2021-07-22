class Link_L:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self, data):
        self.data = data


    def ref(self, head):
        root = Link_L(None)
        start = head
        end = start.next # 3 -> 4 -> 5
        tmp = start.next # 2 -> 3 -> 4 -> 5
        # print('tmp:')
        self.display(tmp)
        # print('end:')
        self.display(end)

        start.next = end.next # 1 -> 4 -> 5
        end.next = end.next.next # 3 -> 5


        print('updated end:')
        self.display(end)
        print('tmp:')
        self.display(tmp)


        start.next.next = tmp


    def display(self, head):
        while head:
            print(head.data)
            head = head.next
        print('--------')



if __name__ == '__main__':
    a = Link_L(1)
    b = Link_L(2)
    c = Link_L(3)
    d = Link_L(4)
    e = Link_L(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e

    a.ref(a)