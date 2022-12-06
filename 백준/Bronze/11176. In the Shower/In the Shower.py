g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    E, N = g()
    print(sum(int(input()) > E for _ in range(N)))