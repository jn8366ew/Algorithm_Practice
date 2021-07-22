import re
a = "A man, a plan, a canal : Panama"

def p(a:str)->bool:
    a = a.lower()
    a = re.sub('[^a-z0-9]', '', a)
    print(a)
    return a == a[::-1]


print(p(a))
