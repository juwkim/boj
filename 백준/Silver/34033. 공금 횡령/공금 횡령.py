import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
cost = {}
for _ in range(N):
    a, b = input().split()
    cost[a] = int(b)

ans = 0
for _ in range(M):
    c, d = input().split()
    ans += 100 * int(d) > 105 * cost[c]
print(ans)