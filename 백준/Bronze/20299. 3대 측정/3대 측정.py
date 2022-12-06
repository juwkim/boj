import sys
g = lambda: map(int, sys.stdin.readline().split())
N, K, L = g()
vip = []
for _ in [0]*N:
    team = [*g()]
    if min(team) >= L and sum(team) >= K:
        vip += team
print(len(vip) // 3)
print(*vip)