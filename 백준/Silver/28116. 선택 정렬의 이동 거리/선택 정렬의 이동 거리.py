import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
A = g()
dic = {num: i for i, num in enumerate(A)}
dist = [0] * N
for i in range(N):
    if A[i] == i + 1:
        continue
    p = dic[i + 1]
    dic[A[p]], dic[A[i]] = i, p
    A[i], A[p] = A[p], A[i]
    d = p - i
    dist[A[i] - 1] += d
    dist[A[p] - 1] += d
print(*dist)