g = lambda: [*map(int, input().split())]


m = int(input())
for _ in range(m):
    Map = [g() for _ in range(5)]
    ans = 0
    for i in range(5):
        for j in range(5):
            
            for s in range(1, 6-i):
                for t in range(1, 6-j):
                    if all(Map[x][y] for x in range(i, i+s) for y in range(j, j+t)):
                        ans = max(ans, s*t)

    print(ans)

    if _ != m - 1:
        input()