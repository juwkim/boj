import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, k = g()
nums = [0] + g()
idx = sorted(range(1, n + 1), key=lambda i: nums[i], reverse=True)[:k]
for i in idx:
    print(i)
for _ in range(k - n):
    print(0)
check = [0] * (n + 1)
for i in idx:
    check[i] = i
for i in range(1, n + 1):
    print(check[i])