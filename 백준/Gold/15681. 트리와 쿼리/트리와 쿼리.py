import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
sys.setrecursionlimit(10**5)
N, R, Q = g()
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    U, V = g()
    tree[U].append(V)
    tree[V].append(U)

ans = [0] * (N + 1)
visited = bytearray(N + 1)
def solve(i):
    visited[i] = 1
    ans[i] = 1
    for j in tree[i]:
        if not visited[j]:
            solve(j)
            ans[i] += ans[j]
solve(R)
for _ in range(Q):
    print(ans[int(input())])