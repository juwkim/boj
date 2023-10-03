import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
check = set("RAKTAS")
A = 0
ans = 0
for c in input():
    if not check and A >= 2:
        break
    ans += 1
    A += c == 'A'
    check.discard(c)
print(ans)