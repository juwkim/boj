g = lambda: [*map(int, input().split())]

from itertools import cycle
for _ in range(int(input())):
    N = int(input())
    cur = 0
    score = 0
    for num in cycle(g()):
        if cur + num <= N:
            cur += num
            score += cur
        if cur == N:
            break
    print(score)