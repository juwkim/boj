def solve(length, x, y):
    if length == 3:
        array[x][y] = "*"
        array[x+1][y-1] = "*"
        array[x+1][y+1] = "*"
        for i in range(-2, 3):
            array[x+2][y+i] = "*"
        return

    length //= 2
    solve(length, x, y)
    solve(length, x + length, y - length)
    solve(length, x + length, y + length)

N = int(input())
array = [[" "]*(2*N-1) for _ in range(N)]
solve(N, 0, N-1)
for line in array:
    print("".join(line))