import sys
input = sys.stdin.readline

for _ in range(int(input())):
    X, Y, x, y = map(int, input().split())
    a = [bytearray(Y) for _ in range(X)]
    ans = 0
    for i in range(X):
        for j in range(Y):
            if a[i][j]:
                continue
            if i + x < X and j + y < Y:
                a[i+x][j+y] = 1
            ans += 1
    print(ans)