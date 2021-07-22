import sys
def f(a):
    s = sys.maxsize
    profit = 0
    for i in a:
        s = min(s, i)
        profit = max(profit, i-s)
    print(profit)

    return profit


f([7,1,5,3,6,4])