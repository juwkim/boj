g = lambda: [*map(int, input().split())]

from bisect import bisect_left
n, k = g()
time = [int(input()) for _ in range(n)]
ans = 0
for i in range(n):
    ans = max(ans, bisect_left(time, time[i] + 1000) - i)
ans = (ans + k - 1) // k
print(ans)