from collections import deque
N, K = map(int, input().split())
deq = deque(range(N, 0, -1))
removed = deque()
for _ in range(N):
    deq.rotate(K-1)
    removed.append(deq.pop())
print(f'<{", ".join(map(str, removed))}>')