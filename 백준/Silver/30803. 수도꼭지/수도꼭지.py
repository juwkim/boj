import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: list(map(int, input().split()))

N = int(input())
A = [0, *g()]
opened = [1] * (N + 1)
cur = sum(A)
print(cur)
for _ in range(int(input())):
    query = g()
    if len(query) == 2:
        _, i = query
        opened[i] ^= 1
        if opened[i]:
            cur += A[i]
        else:
            cur -= A[i]
    else:
        _, i, x = query
        if opened[i]:        
            cur += x - A[i]
        A[i] = x
    print(cur)