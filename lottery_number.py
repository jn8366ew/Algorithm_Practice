import random


a = [i for i in range(1, 46)]
c = []
random.shuffle(a)
for i in range(5):
    b = [a[i] for i in range(6)]
    c.append(sorted(b))
    random.shuffle(a)

print(c)
