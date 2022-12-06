from collections import deque
g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    N = int(input())
    dq = deque([1])
    while True:
        num = dq.popleft()
        if num % N == 0 and all(i in '01' for i in str(num)):
            print(num)
            break
        dq.append(num * 10)
        dq.append(num * 10 + 1)