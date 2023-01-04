while N:= int(input()):
    mat = [bytearray(102) for _ in range(102)]
    ans = 0
    for _ in range(N):
        x, y = map(lambda num: int(num) + 1, input().split())
        mat[x][y] = 1
        ans += 2 * sum(mat[i][j] == 0 for i, j in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))) - 4
    print(ans)