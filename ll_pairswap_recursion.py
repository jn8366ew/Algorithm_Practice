
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

    def swapPair(self, head):
        if head and head.next:
            p = head.next
            head.next = self.swapPair(p.next)
            p.next = head
            return p
        return head

    def oddevenPair(self, head):

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = even_head

        return head






a = Link_L(1)
b = Link_L(2)
c = Link_L(3)
d = Link_L(4)
e = Link_L(5)
f = Link_L(6)


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
e.next = f
# f.next = g


# a.display(a.oddevenPair(a))

a.swapPair(a)

# a.display(a.swapPair(a))