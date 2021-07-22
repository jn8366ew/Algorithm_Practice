import collections


class ll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def add(self, data):
        new_node = self.Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def pal(self, head):
        node = head
        q = collections.deque()
        while node:
            q.append(node.data)
            node = node.next
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    def elepal(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            # None -> 1-None -> 2-1-None...
            # 첫 rev는 'a' rev.next는 None,
            # 즉 오른쪽의 rev는 기존의 rev를 가르킨다.
            rev, rev.next, slow = slow, rev, slow.next

            # 실험 3중할당 안할경우 -> slow는 기존의 rev가 참조하던 None을 참조하게 됨
            # rev, rev.next, = slow, rev
            # slow = slow.next

        if fast:
            slow = slow.next

        while rev and rev.data == slow.data:
            slow, rev = slow.next, rev.next
        return not rev

a = ll()
a.add('a')
a.add('b')
a.add('a')

print(a.pal(a.head))
print(a.elepal(a.head))


