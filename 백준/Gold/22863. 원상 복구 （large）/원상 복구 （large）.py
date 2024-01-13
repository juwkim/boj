import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
S = g()
D = [*map(lambda x: int(x) - 1, input().split())]
ans = [0] * N
for i in range(N):
    if ans[i]:
        continue
    cycle = [i]
    now = i
    while D[now] != i:
        now = D[now]
        cycle.append(now)
    for idx in range(len(cycle)):
        from_idx = cycle[idx]
        to_idx = cycle[(idx + K) % len(cycle)]
        ans[to_idx] = S[from_idx]
print(*ans)