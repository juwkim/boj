import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

L, N, T = g()
box = [[] for _ in range(L + 1)]
for _ in range(N):
    S, C = input().split()
    C = [-1, 1][C == 'R']
    box[int(S)].append(C)
ans = 0
for _ in range(T):
    new = [[] for _ in range(L + 1)]
    for i in range(L + 1):
        for j in box[i]:
            new[i + j].append(j)
    if new[0]:
        new[0] = [1]
    if new[L]:
        new[L] = [-1]
    ans += sum(len(new[i]) == 2 for i in range(1, L))
    box = new
print(ans)