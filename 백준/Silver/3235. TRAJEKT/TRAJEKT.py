from collections import deque
input = __import__('sys').stdin.readline

time = sum(map(int, input().split()))

A = deque()
for _ in range(int(input())):
    h, m = map(int, input().split(':'))
    A.append(h * 60 + m)

B = deque()
for _ in range(int(input())):
    h, m = map(int, input().split(':'))
    B.append(h * 60 + m)

A_wait, B_wait = deque(), deque()
if A[0] < B[0]:
    B_wait.append(A.popleft() + time)
else:
    A_wait.append(B.popleft() + time)

while A and B:
    if A[0] < B[0]:
        if A_wait and A_wait[0] <= A[0]:
            A_wait.popleft()
        B_wait.append(time + A.popleft())
    else:
        if B_wait and B_wait[0] <= B[0]:
            B_wait.popleft()        
        A_wait.append(time + B.popleft())

while A:
    if A_wait and A_wait[0] <= A[0]:
        A_wait.popleft()
    B_wait.append(time + A.popleft())

while B:
    if B_wait and B_wait[0] <= B[0]:
        B_wait.popleft()
    A_wait.append(time + B.popleft())

ans = len(A_wait) + len(B_wait)
print(ans)