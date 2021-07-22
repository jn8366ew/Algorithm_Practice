from Stack import Stack


def valid(s:str) -> bool:
    l = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char not in l:
            l.append(char)
        elif not l or table[char] != l.pop():
            return False

    return True

print(valid('[](){}'))


a = Stack()
a.push('(')
a.push('[')
a.push('{')

print(a.valid('}])'))
