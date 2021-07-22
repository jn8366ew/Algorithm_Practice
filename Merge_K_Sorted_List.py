import heapq
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



def mergeKLists(lists: List[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = []

    # 각 연결 리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        if lists[i]:
            # heap에 저장하고, 저장할 객체로는 노드 값, i, 그리고 리스트 객체들이다.
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    # 힙 추출 이후 다음 노드는 다시 저장
    print(heap)
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]

        result.next = node[2]
        print('node:', node, 'idx:', idx, 'result.next:', result.next)

        result = result.next
        if result.next:
            print('result.next: ', result.next.val, 'idx:', idx)
            heapq.heappush(heap, (result.next.val, idx, result.next))

    return root.next


if __name__ == "__main__":
    k, l1 = [], []
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(5)
    a.next, b.next = b, c

    x = ListNode(1)
    y = ListNode(3)
    z = ListNode(4)
    x.next, y.next = y, z

    n = ListNode(2)
    m = ListNode(6)
    n.next = m


    k.append(a)
    k.append(x)
    k.append(n)

    q = mergeKLists(k)

    while q:
        print(q.val)
        q = q.next