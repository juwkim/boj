import sys
g = lambda: map(int, sys.stdin.readline().split())

n, m = g()
buy = [0] * (m + 1)
for i in range(1, n + 1):
    k, *nums = g()
    for num in nums:
        if buy[num] == 0:
            buy[num] = i
            m -= 1
if m:
    print("NO")
else:
    print("YES")
    print(*range(n, 0, -1))
    print(*buy[1:])