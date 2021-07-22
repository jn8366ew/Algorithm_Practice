class Link_L:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self, data):
        self.data = data


    def runner_pal(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.data == slow.data:
            slow, rev = slow.next, rev.next

        return not rev

    def aa(self, head):
        def reverse(node, prev=None):
            if node:
                next, node.next = node.next, prev
                return reverse(next, node)
            return prev


        return reverse(head)


a = Link_L(1)
b = Link_L(2)
c = Link_L(3)
d = Link_L(4)
e = Link_L(5)

a.next = b
b.next = c
c.next = d
d.next = e


k = a.aa(a)

while k:
    print(k.data)
    k = k.next

