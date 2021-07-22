import collections


def remove_du(s):
    stack = []
    counter = collections.Counter(s)
    seen = set()

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        # 현재 문자 char가 스택에 쌓여있는 문자(이전 문자보다 앞선)이고
        # 뒤에 다시 붙일 문자가 남아 있다면 -> True
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())

        stack.append(char)
        seen.add(char)

    return ''.join(stack)

print(remove_du('bcabc'))
print(remove_du('cbacdcbc'))