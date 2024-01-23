import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
A = [int(input()) for _ in range(n)]
B = [i for i in range(1, 2 * n + 1) if i not in A]
cur = 0
while A and B:
    l = [(A[i], i) for i in range(len(A)) if A[i] > cur]
    if l:
        cur, idx = min((A[i], i) for i in range(len(A)) if A[i] > cur)
        A.pop(idx)
        if not A:
            break
    else:
        cur = 0
    l = [(B[i], i) for i in range(len(B)) if B[i] > cur]
    if l:
        cur, idx = min((B[i], i) for i in range(len(B)) if B[i] > cur)
        B.pop(idx)
    else:
        cur = 0
print(len(B))
print(len(A))