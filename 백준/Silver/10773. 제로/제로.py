from collections import deque
deq = deque()
for _ in range(int(input())):
    n = int(input())
    if n:
        deq.append(n)
    else:
        deq.pop()
print(sum(deq))