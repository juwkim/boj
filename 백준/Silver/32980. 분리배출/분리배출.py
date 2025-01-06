import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
trash = [input() for _ in range(N)]
cost = {k: v for k, v in zip("PCVSGF", map(int, input().split()))}
cost['O'] = int(input())
for k, v in cost.items(): cost[k] = min(cost[k], cost['O'])
ans = 0
for s in trash:
    if s[0] == 'O' or len({*s}) > 1:
        ans += cost['O'] * len(s)
    else:
        ans += cost[s[0]] * len(s)
print(ans)