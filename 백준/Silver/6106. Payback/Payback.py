import sys
input = sys.stdin.readline

N = int(input())
idx, debt = -1, 0
ans, money = N, 0
for i in range(N):
    cur = int(input())
    if cur < 0:
        cur = -cur
        if money >= cur:
            money -= cur
        else:
            debt += cur
            if idx == -1:
                idx = i
    else:
        money += cur
        if 0 < debt <= money:
            money -= debt
            debt = 0
            ans += 2 * (i - idx)
            idx = -1
print(ans)