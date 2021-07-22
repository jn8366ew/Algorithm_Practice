import itertools


def f(n, k):
    result = []

    def dfs(elements, start, k):
        if k == 0:
            result.append(elements[:])
            return
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()
    dfs([], 1, k)
    return result

def c(n, k):
    return list(itertools.combinations(range(1, n+1), k))



print(f(4, 2))
print(c(4, 2))


