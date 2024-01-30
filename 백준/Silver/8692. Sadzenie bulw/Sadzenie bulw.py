import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
b = sorted(g(), reverse=True)
m = int(input())
ans = 0
for bi in b:
    if m <= bi:
        ans += m ** 2
        break
    m -= bi
    ans += bi ** 2
print(ans)