N, M = map(int, input().split())
bulbs = [*map(int, input().split())]
for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        bulbs[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            bulbs[i] = 1 - bulbs[i]
    elif a == 3:
        for i in range(b-1, c):
            bulbs[i] = 0
    else:
        for i in range(b-1, c):
            bulbs[i] = 1
print(*bulbs)