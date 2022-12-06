from collections import deque
for _ in range(int(input())):
    N, M = map(int, input().split())
    deq = deque(input().split())
    count = 0
    while True:
        if any(deq[0] < deq[i] for i in range(1, len(deq))):
            deq.rotate(-1)
            M = (M - 1) % len(deq)
        else:
            deq.popleft()
            count += 1
            if M == 0:
                break
            M = (M - 1) % len(deq)
    print(count)