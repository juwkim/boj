g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    N = int(input())
    Map = [g() for _ in range(N)]
    ans = 0
    for x in range(N):
        num = sum(Map[x+y][y] for y in range(N-x))
        ans = max(ans, num)
    for y in range(1, N):
        num = sum(Map[x][x+y] for x in range(N-y))
        ans = max(ans, num)

    print(f'Case #{_}: {ans}')