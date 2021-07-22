can = [2,3,6,7]
tar = 7

def f(c, t):
    result = []

    def dfs(csum, index, path):
        if csum < 0:
            return

        if csum == 0:
            result.append(path)
            return

        for i in range(index, len(c)):
            dfs(csum - c[i], i, path + [c[i]])

    dfs(t, 0, [])
    return result

