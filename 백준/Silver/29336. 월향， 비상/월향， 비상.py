import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
A = sorted(g())
ans = 0
for _ in range(M):
    T, Q = g()
    while A and ans < Q:
        ans += A.pop() + T
    if ans < Q:
        ans = -1
        break
if ans != -1:
    ans += sum(num + T for num in A)
print(ans)