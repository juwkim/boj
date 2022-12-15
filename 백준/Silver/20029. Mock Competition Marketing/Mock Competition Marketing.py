def bid(tactic):
    cnt, money = 0, K
    min_cost = min(cost[x] for x in range(6) if tactic & (1 << x))
    for x in auction:
        if (tactic & (1 << x)) and money >= cost[x]:
            money -= cost[x]
            cnt += 1
        if money < min_cost:
            break
    return cnt

g = lambda: [*map(int, input().split())]
N, K = g()
cost = g()
auction = [int(x) - 1 for x in input().split()]
ans = 0
for i in range(1, 64):
    ans = max(ans, bid(i))
print(ans)