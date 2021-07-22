import re
import collections

def a(s:str, ban:str) -> str:
    k = [x for x in re.sub(r'[^\w]', ' ', s).lower().split() if x not in ban]
    print(k)
    c = collections.Counter(k)
    return c.most_common(1)[0][0]


print(a("Bob hit a ball, the hit BALL flew far after it was hit.", "ball"))


a = ['cde', 'cfc', 'abc']
a.sort(key= lambda x: (x[0], x[-1]))
print(a)

a = ['cde', 'cfc', 'abc']
a.sort(key= lambda x: (x[0], x[1]))
print(a)

