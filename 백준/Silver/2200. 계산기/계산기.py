import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
ans = 2
_, *l, e = input().split()
for p in l:
    if p == '0':
        ans += 2
    else:
        ans += 3 + len(p)
if e != '0':
    ans += 1 + len(e)
print(ans)