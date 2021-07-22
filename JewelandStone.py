def f(j, s):
    freq = {}
    count = 0

    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    for char in j:
        if char in freq:
            count += freq[char]
    return count

def ele(j, s):
    return sum(x in j for x in s)


print(f("aA", "aAAbbbb"))
print(ele("aA", "aAAbbbb"))