g = lambda: [*map(int, input().split())]

N, K = g()
nations = []
for _ in range(N):
    num, *medals = g()
    nations.append(medals)
    if num == K:
        target = medals
nations.sort(reverse=True)
for i in range(N):
    if nations[i] == target:
        print(i + 1)
        break