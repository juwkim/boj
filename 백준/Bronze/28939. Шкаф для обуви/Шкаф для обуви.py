import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
k, m1, m2 = g()
ans = 0
for _ in range(n):
    h, _, *nums = g()
    for num in nums:
        if num * m1 < h or num * m2 > h * k:
            ans += 1
print(ans)