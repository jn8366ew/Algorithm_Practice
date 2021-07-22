
def rd(s:str)->str:
    for char in sorted(set(s)):
        su = s[s.index(char):]

        if set(s) == set(su):
            return char + rd(su.replace(char, ''))

    return ''


print(rd('cbacdcbc'))