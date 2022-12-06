g = lambda: [*map(int, input().split())]

E, S, M = g()
E -= 1
S -= 1
M -= 1
for i in range(15 * 28 * 19):
    if i % 15 == E and i % 28 == S and i % 19 == M:
        print(i + 1)
        break