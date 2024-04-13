import heapq

N = int(input())
A = int(input())
V = [-int(input()) for _ in range(N - 1)]
heapq.heapify(V)
d, a = A, -1
while -(a:=heapq.heappushpop(V, a + 1)) >= A:
    A += 1
print(A - d)