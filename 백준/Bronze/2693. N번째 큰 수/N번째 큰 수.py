g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    print(sorted(g())[-3])