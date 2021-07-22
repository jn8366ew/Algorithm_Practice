import statistics
import sys

nums = [-1, 0, 1, 2, -1, -4]
res = []

# 정렬된 상태
nums.sort()
for i in range(len(nums) - 2):
    # i의 중복 예외 처리
    if i > 0 and nums[i] == nums[i-1]:
        continue
    l, r = i + 1, len(nums) - 1


    while l < r:
        # 체크
        total = nums[i] + nums[l] + nums[r]

        if total < 0:
            l += 1

        elif total > 0:
            r -= 1

        else:
            res.append([nums[i], nums[l], nums[r]])

            while l < r and nums[l] == nums[l+1]:
                l += 1
            while l < r and nums[r] == nums[r-1]:
                r -= 1

            l += 1
            r -= 1


print(res)



# 배열 파티션

a = [1,4,3,2]

a.sort
print(sum(a[::2]))

# a3
a = None
a = [1,2,3,4]

# 자기자신을 제외한 배열의 곱
res = None

res = []
n = 1

for i in range(len(a)):
    res.append(n)
    n = n * a[i]


n = 1
for i in range(len(a) - 1, -1, -1):
    res[i] = res[i] * n
    n = n * a[i]

print(res)

a = None

# 주식 팔기
a = [7, 1, 5, 3, 6, 4]

min_price = sys.maxsize
profit = 0

for price in a:
    min_price = min(min_price, price)
    profit = max(profit, price-min_price)

print(profit)


