import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
A = g()
B = sorted(g())

order = sorted(range(N), key=lambda i: A[i])
ans = [-1] * N
for i in range(N):
    if A[order[i]] > B[i]:
        print(-1)
        exit()
    ans[order[i]] = B[i]
print(*ans)