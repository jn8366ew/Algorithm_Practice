

def solution(A):
    # k = [x for x in set(A)]
    # g = max(k)
    #
    # if g > 0:
    #     for i in range(1, g):
    #         if i not in k:
    #             return i
    #
    # else:
    #     return 1
    #
    # return g+1



    max_A = max(A)
    B = set([a if a >= 0 else 0 for a in A])
    b = 1
    if max_A <= 0:
        return 1
    else:
        while b in B:
            b += 1
        return b








k = [1,3,6,4,1,2]
print(solution(k))

k = [-1, -3]
print(solution(k))


k = [1, 2, 3]
print(solution(k))
