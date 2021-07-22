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



    def reverse(self, head):
        node, prev = head, None

        while node:
            # 1. next = 헤드 노드의 다음
            # 2. 그 헤드 노드의 다음 링크를 None
            # 3. prev 노드는 방금 업뎃 시킨 노드로
            # 4. 노드는 다음 노드로 갱신
            # 5. next는 4의 노드 링크된 노드로 그리고 2~5번 반복...
            next, node.next = node.next, prev
            prev, node = node, next

        return prev


    def ll_to_list(self, head):
        node = head
        l_list = []
        while node:
            l_list.append(node.data)
            node = node.next
        return l_list

    def list_to_ll(self, l_list:list):
        new_ll = ll()

        for i in l_list:
            new_ll.add(i)
        return new_ll

    def check_ll(self, head):
        node = head
        while node:
#            print(node.data)
            node = node.next

    def sun_two_ll(self, head1, head2):
        a = self.ll_to_list(self.reverse(head1))
        b = self.ll_to_list(self.reverse(head2))

        # print(int(''.join(str(e) for e in a)))
        #
        # print(int(''.join(str(e) for e in b)))

        resultStr = int(''.join(str(e) for e in a)) + \
                        int(''.join(str(e) for e in b))

        self.check_ll(self.list_to_ll(str(resultStr)).head)
        return self.list_to_ll(str(resultStr))




class Link_L:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self, data):
        self.data = data


    def ele_sum(self, head1, head2):
        carry = 0
        root = head = Link_L(0)

        while head1 or head2 or carry:
            sum = 0
            if head1:
                sum += head1.data
                head1 = head1.next

            if head2:
                sum += head2.data
                head2 = head2.next

            # carry, val = divmod(sum + carry, 10)
            # 만약 내가 divmod를 모른다고 했을 때
            if carry > 0:
                sum += 1
            carry = int(sum / 10)
            val = int(sum % 10)
            # print(carry, val)
            # 결과값 기존 링크드 리스트에 링크
            head.next = Link_L(val)

            # 내가 divmode를 모른다고 했을 때

            # 기존 헤드 포인터를 위에 만든 노드로 갱신
            head = head.next

        return root.next



#
# a = ll()
# a.add(2)
# a.add(4)
# a.add(3)
#
# b = ll()
# b.add(5)
# b.add(6)
# b.add(4)
#
#
# print(a.sun_two_ll(a.head, b.head))
#
# a, b = None, None
#
# a = Link_L(2)
# b = Link_L(4)
# c = Link_L(3)
#
# a.next = b
# b.next = c
#
# x = Link_L(5)
# y = Link_L(6)
# z = Link_L(4)

#
# x.next = y
# y.next = z
#
# result = a.ele_sum(a, x)
#
#
# while result:
#     print(result.data)
#     result = result.next
