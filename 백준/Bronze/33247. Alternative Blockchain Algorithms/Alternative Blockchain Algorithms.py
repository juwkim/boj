import sys
input = sys.stdin.readline

ans, prv = 0, 0
for _ in range(int(input())):
    i, p, m = map(int, input().split())
    if p != prv:
        ans = "INVALID"
        break
    ans += m
    if ans < 0:
        ans = "NO_MONEY"
        break
    prv = i
print(ans)