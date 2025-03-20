import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, n = map(int, input().split())
    a = [input() for _ in range(m)]
    d, i = {"".join(a): 0}, 1
    while True:
        new_a = [["" for _ in range(n)] for _ in range(m)]
        for x in range(m):
            for y in range(n):
                cnt = 0
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0:
                            continue
                        cnt += a[(x + dx) % m][(y + dy) % n] == 'o'
                if cnt <= 1:
                    new_a[x][y] = 'x'
                elif cnt == 2:
                    new_a[x][y] = a[x][y]
                elif cnt == 3:
                    new_a[x][y] = 'o'
                else:
                    new_a[x][y] = 'x'        
        a = ["".join(row) for row in new_a]
        s = "".join(a)
        if s in d:
            break
        d[s] = i
        i += 1
    print(i - d[s])