g = lambda: [*map(int, input().split())]

N = int(input())
A, B = g(), sorted(g())
order = sorted(range(N), key=lambda i: A[i])
if any(A[order[i]] > B[i] for i in range(N)):
    print(-1)
else:
    for i in range(N):
        A[order[i]] = B[i]
    print(*A)