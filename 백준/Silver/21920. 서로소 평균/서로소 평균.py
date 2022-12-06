from math import gcd
input()
nums = [*map(int, input().split())]
X = int(input())
Sum, cnt = 0, 0
for num in nums:
    if gcd(X, num) == 1:
        cnt += 1
        Sum += num
print(Sum / cnt)  