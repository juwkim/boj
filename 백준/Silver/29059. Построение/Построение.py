import sys
g = lambda: map(int, sys.stdin.readline().split())

n, m = g()
max_len = 1
for _ in range(m):
    l, r = g()
    max_len = max(max_len, r - l + 1)
print(max_len)
print(*[i % max_len + 1 for i in range(n)])