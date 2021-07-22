import collections

q = collections.deque()
q.append(1)
print(q)


for _ in range(len(q)-1):
    q.append(q.popleft)


print(q)



a = []
b = [2]
print(a+b)