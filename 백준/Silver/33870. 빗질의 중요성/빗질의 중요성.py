g = lambda: [*map(int, input().split())]

N, M = g()
A = g()
dogs = [[0, False] for _ in range(N)]
for day, B in enumerate(g(), 1):
    B -= 1
    if dogs[B][1]:
        dogs[B][1] = day != dogs[B][0] + 1
    elif day - dogs[B][0] > A[B]:
        dogs[B][1] = True
    dogs[B][0] = day
print(sum(dogs[i][1] or (M + 1 - dogs[i][0] > A[i]) for i in range(N)))