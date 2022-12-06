g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    n, k = g()
    print(sorted(g())[k-1])