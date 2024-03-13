g = lambda: sorted(map(int, input().split()))

K = int(input())
N = int(input())
A = g()
M = int(input())
B = g()
ans = 0
for i in range(N):
    for j in range(M):
        ans += A[i] + K == B[j]
print(ans)