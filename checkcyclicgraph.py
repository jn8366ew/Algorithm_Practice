import collections


def f(numCourses, prerequisites):
    graph = collections.defaultdict(list)

    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):
        if i in traced:return False

        if i in visited:return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False

        traced.remove(i)
        visited.add(i)

        return True
    for x in list(graph):
        if not dfs(x):
            return False

    return True


a = 2
b = [[1, 0]]
c = [[1, 0], [0, 1]]
d = [[0, 1], [2, 0], [1, 2]]
e = [[0, 1], [0, 2], [1, 2], [2, 0]]
print(f(a, b))
print(f(a, c))
print(f(a, d))
print(f(a, e))

