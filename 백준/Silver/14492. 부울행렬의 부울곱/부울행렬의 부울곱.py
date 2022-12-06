G = lambda: [*map(int, input().split())]
I = lambda: int(input())
N = I()
A = [G() for _ in range(N)]
B = [G() for _ in range(N)]
B = [*zip(*B)]
C = [[] for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        ans += any(a + b == 2 for a, b in zip(A[i], B[j]))
print(ans)