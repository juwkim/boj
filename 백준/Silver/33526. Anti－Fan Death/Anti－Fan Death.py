N = int(input())
a = [3 * N * ['A'] for _ in range(3 * N)]

def fill(x, y, c):
    for i in range(x, x + N):
        for j in range(y, y + N):
            a[i][j] = c
fill(0, 0, 'N')
fill(N, 2 * N, 'N')
fill(2 * N, N, 'N')
fill(0, 2 * N, 'Z')
fill(N, N, 'Z')
fill(2 * N, 0, 'Z')

for l in a:
    print(*l, sep='')