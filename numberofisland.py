a = [['1','1','1','1','0'],
     ['1','1','0','1','0'],
     ['1','1','0','0','0'],
     ['0','0','0','0','0']]

b = [['1','1','0','0','0'],
     ['1','1','0','0','0'],
     ['0','0','1','0','0'],
     ['0','0','0','1','1']]


c = [['1','1','0'],
     ['1','1','0'],
     ['0','0','1']]


def f(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or \
                j < 0  or j >= len(grid[0]) or \
                grid[i][j] != '1':
            return

        grid[i][j] = 0
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                print("DFS 종료")
                count += 1
    return count

# print(f(a))


# print(f(b))

print(f(c))