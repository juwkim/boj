import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
A = g()
ans = 0
for i in range(N - 1):
    if A[i + 1] > A[i]:
        continue
    if A[i + 1] + K <= A[i]:
        ans = -1
        break
    A[i + 1] += K
    ans += 1
print(ans)