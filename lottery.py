import random

a = []
b = []
for i in range(5):

    while len(b) < 6:
        n = random.randrange(start=1, stop=45)
        if n in b:
            continue
        b.append(n)
    a.append(b)
    b.sort()
    b = []

print(a)