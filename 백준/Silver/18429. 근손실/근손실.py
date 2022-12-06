g = lambda: map(int, input().split())

N, K = g()
A = tuple(g())
ans = 0
visited = [0] * N
def solve(idx, iteration, weight):
    global ans
    
    if visited[idx]:
        return
    
    weight += A[idx] - K
    if weight < 500:
        return
    
    if iteration == N:
        ans += 1
        return
    
    visited[idx] = 1
    for i in range(N):
        solve(i, iteration + 1, weight)
    visited[idx] = 0
    
for idx in range(N):
    solve(idx, 1, 500)
print(ans)