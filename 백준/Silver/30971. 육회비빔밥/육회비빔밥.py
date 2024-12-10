from itertools import permutations
g = lambda: [*map(int, input().split())]

N, K = g()
A, B, C = g(), g(), g()
ans = -1
for l in permutations(range(N)):
    if any(C[l[i]] * C[l[i + 1]] > K for i in range(N - 1)):
        continue
    ans = max(ans, sum(A[l[i]] * B[l[i + 1]] for i in range(N - 1)))
print(ans)