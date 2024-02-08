import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
A = [int(input()) for _ in range(N)]
B = {int(input()): i for i in range(N)}
l = []
visited = bytearray(N + 1)
for i in range(N):
    if visited[i]:
        continue
    pos = i
    visited[pos] = 1
    cnt = 1
    while not visited[B[A[pos]]]:
        visited[B[A[pos]]] = 1
        pos = B[A[pos]]
        cnt += 1
    if cnt > 1:
        l.append(cnt)
print(len(l), max(l) if l else -1)