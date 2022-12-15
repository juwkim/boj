g = lambda: [*map(int, input().split())]
N = int(input())
A, B = g(), g()
P = [sum(A[i::3]) for i in range(3)]
Q = [sum(B[i::3]) for i in range(3)]
ans = [0, 0, 0]
for i in range(3):
    for j in range(3):
        ans[(i + j - 1) % 3] += P[i] * Q[j]
print(*ans)