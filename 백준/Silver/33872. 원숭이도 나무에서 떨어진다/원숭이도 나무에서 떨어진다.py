import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, H = g()
S, E = map(lambda x: int(x) - 1, input().split())
B = g()
K = g()
tree = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(lambda x: int(x) - 1, input().split())
    tree[u].append(v)
    tree[v].append(u)

ans = -1
cnt = [0] * N
cnt[S] = 1
def solve(cur, energy, banana):
    global ans
    if energy == 0:
        if cur == E:
            ans = max(ans, banana)
        return
    for nxt in tree[cur]:
        if K[nxt] == 0 and cnt[nxt] != 2:
            cnt[nxt] += 1
            nxt_banana = banana + B[nxt]
            tmp = B[nxt]
            B[nxt] = 0
            solve(nxt, energy - 1, nxt_banana)
            B[nxt] = tmp
            cnt[nxt] -= 1
banana = B[S]
B[S] = 0
solve(S, H, banana)
print(ans)