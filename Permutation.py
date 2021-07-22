import itertools

a = [1,2,3]


def f(nums):
    result = []
    prev_elements = []

    def dfs(elements):
        if len(elements) == 0:
            result.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return result


print(f(a))


def per(nums):
    return list(itertools.permutations(nums))

print(per(a))