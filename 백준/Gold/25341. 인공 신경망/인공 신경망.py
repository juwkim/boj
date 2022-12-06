import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]

N, M, Q = g()

nums = [g() for _ in range(M)]
*out, B = g()

P = [0] * N
for i in range(M):
    c, *l, b = nums[i]
    B += out[i] * b
    for j in range(c):
        P[l[j] - 1] += out[i] * l[j + c]
for _ in range(Q):
    print(sum(a * b for a, b in zip(P, g())) + B)