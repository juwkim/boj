import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r, c = map(int, input().split())
    a = [input() for _ in range(r)]
    ans = 0
    for i in range(r):
        for j in range(c):
            for di, dj in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                if 0 <= i + 3 * di < r and 0 <= j + 3 * dj < c and all(a[i + k * di][j + k * dj] == char for char, k in zip("word", range(4))):
                    ans += 1
    print(ans)