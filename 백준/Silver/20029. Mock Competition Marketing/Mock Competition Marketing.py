def bid(tactic):
    cnt, budget = 0, K
    for x in auction:
        if (tactic & (1 << x)) and budget >= cost[x]:
            budget-= cost[x]
            cnt += 1
    return cnt

g = lambda: [*map(int, input().split())]
N, K = g()
cost = g()
auction = [int(x) - 1 for x in input().split()]
ans = 0
for i in range(64):
    ans = max(ans, bid(i))
print(ans)