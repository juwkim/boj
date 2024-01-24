import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
a = g()
b = g()
ans = 0
for i in range(N - 1):
    if a[i] == b[i]:
        continue
    ans += 1
    a[i + 1] ^= a[i] ^ b[i]
if a[-1] != b[-1]:
    ans = -1
print(ans)