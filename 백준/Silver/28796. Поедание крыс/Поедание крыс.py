import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, k = g()
ans = 0
for num in g():
    if ans + num > k:
        break
    ans += num
print(ans)