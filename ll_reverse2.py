class Link_L:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self, data):
        self.data = data

    def display(self, head):

        while head:
            print(head.data)
            head = head.next

    def reverse(self, head, m, n):
        root = start = Link_L(None)
        root.next = head


        for _ in range(m - 1):
            start = start.next
        end = start.next

        for _ in range(n - m):
            temp = start.next # temp는 start.next를 참조
            start.next = end.next # start.next는 end.next를 참조
            end.next = end.next.next # end.next는 end.next.next를 참조
            start.next.next = temp # 결과적으로 temp은 end.next를 참조하게 된다.

            print('temp addr: ', id(temp), 'temp.next addr:', id(temp.next), 'end addr: ', id(end), 'end.next addr:', id(end.next))
        return root.next



if __name__ == '__main__':

    a = Link_L(1)
    b = Link_L(2)
    c = Link_L(3)
    d = Link_L(4)
    e = Link_L(5)


    # a = Link_L(2)
    # b = Link_L(1)
    # c = Link_L(3)
    # d = Link_L(5)
    # e = Link_L(6)
    # f = Link_L(4)
    # g = Link_L(7)
    #


    a.next = b
    b.next = c
    c.next = d
    d.next = e
    # e.next = f
    # f.next = g

    a.reverse(a, 2, 4)
    a.display(a)

    # a.display(a.oddevenPair(a))

    # a.swapPair(a)

    # a.display(a.swapPair(a))


