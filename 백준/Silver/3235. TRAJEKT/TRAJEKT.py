import heapq
from collections import deque
input = __import__('sys').stdin.readline

def g(): return [*map(int, input().split())]

time = sum(g())

A = deque()
for _ in range(int(input())):
    h, m = map(int, input().split(':'))
    A.append(h * 60 + m)

B = deque()
for _ in range(int(input())):
    h, m = map(int, input().split(':'))
    B.append(h * 60 + m)

A_wait, B_wait = [], []
if A[0] < B[0]:
    B_wait.append(A.popleft() + time)
else:
    A_wait.append(B.popleft() + time)

heapq.heapify(A_wait)
heapq.heapify(B_wait)

while A and B:
    if A[0] < B[0]:
        if A_wait and A_wait[0] <= A[0]:
            heapq.heappop(A_wait)        
        heapq.heappush(B_wait, time + A.popleft())
    else:
        if B_wait and B_wait[0] <= B[0]:
            heapq.heappop(B_wait)        
        heapq.heappush(A_wait, time + B.popleft())

while A:
    if A_wait and A_wait[0] <= A[0]:
        heapq.heappop(A_wait)        
    heapq.heappush(B_wait, time + A.popleft())

while B:
    if B_wait and B_wait[0] <= B[0]:
        heapq.heappop(B_wait)        
    heapq.heappush(A_wait, time + B.popleft())

ans = len(A_wait) + len(B_wait)
print(ans)    