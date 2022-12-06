import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]
N, Q = g()
A = g()
for _ in range(Q):
    op, *l = g()
    i, j = l[0] - 1, l[1] - 1
    if op == 1:
        print(sorted(A[i:j+1])[l[2]-1])
    else:
        A[i], A[j] = A[j], A[i]