import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, K = g()
A, B = g(), g()
ans = sum(a == b for a, b in zip(A, B))
def solve(cnt):
    global ans
    if cnt == K:
        return
    for i in range(N):
        if B[i] == 0:
            continue
        last = B[-1]
        for j in range(N-1, i, -1):
            B[j] = B[j-1]
        B[i] = 0
        ans = max(ans, sum(a == b for a, b in zip(A, B)))
        solve(cnt + 1)
        for j in range(i, N-1):
            B[j] = B[j+1]
        B[-1] = last
        
        cur = B[i]
        for j in range(i, N-1):
            B[j] = B[j+1]
        B[-1] = 0
        ans = max(ans, sum(a == b for a, b in zip(A, B)))
        solve(cnt + 1)
        for j in range(N-1, i, -1):
            B[j] = B[j-1]
        B[i] = cur
solve(0)
print(ans)