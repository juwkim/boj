import heapq

N, A, *votes = map(int, open(0).read().split())
votes = [-v for v in votes]
heapq.heapify(votes)
dasom, num = A, -1
while -(num:=heapq.heappushpop(votes, num + 1)) >= A:
    A += 1
print(A - dasom)