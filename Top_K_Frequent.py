import collections
import heapq

def f(l, k):
    freqs = collections.Counter(l)
    freqs_heap = []
    print(freqs)
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    print(freqs_heap)
    topk = list()

    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    return topk

l = [1,1,1,2,2,3]
k = 2

f(l, k)