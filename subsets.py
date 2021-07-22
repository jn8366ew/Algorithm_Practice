def f(nums):
    result = []

    def dfs(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i+1, path + [nums[i]])

    dfs(0, [])
    return result


print(f([1,2,3]))

