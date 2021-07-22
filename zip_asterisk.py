# zip
import collections

a = [1,2,3,4,5]
b = [2,3,4,5]
c = [3,4,5]

print(list(zip(a,b)))
print(list(zip(b,c)))
print(list(zip(a,b,c)))


a = ['a1', 'a2']
b = ['b1', 'b2']
c = ['c1', 'c2']
d = ['d1', 'd2']

print(list(zip(a,b,c,d)))


l = [1,1,1,2,2,3]
k = 2

print(collections.Counter(l).most_common(k))
print(list(zip(*collections.Counter(l).most_common(k))))
print(list(zip(collections.Counter(l).most_common(k))))


f = ['q', 'a', 'c', 'z']

print(*f)

def f1(*params):
    print(params)

f1(*f)

# 아스테리스크 활용하기
a, *b = [1,2,3,4]
print(a)
print(b)

*a, b = [1,2,3,4]
print(a)
print(b)

# 키/값 페어 언패킹
d = {'year': '2020', 'month': '01', 'day': '7'}
nd = {**d, 'day': '14'}
print(nd)