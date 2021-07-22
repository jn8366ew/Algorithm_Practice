
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

    def pair_swap_only_value(self, head):
        cur = head

        while cur and cur.next:
            cur.data, cur.next.data = cur.next.data, cur.data
            cur = cur.next.next

        return head

    def pair_swap_while_loop(self, head):
        root = prev = Link_L(None)
        prev.next = head
        while head and head.next:
            x = head.next
            head.next = x.next
            x.next = head


            # 1-2-1-3-4
            prev.next = x

            #
            head = head.next
            prev = prev.next.next


        return root.next


a = Link_L(1)
b = Link_L(2)
c = Link_L(3)
d = Link_L(4)


a.next = b
b.next = c
c.next = d


#a.pair_swap_only_value(a)
f = a.pair_swap_while_loop(a)
a.display(f)



