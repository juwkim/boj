n, m = map(int, input().split())
a = ['*' * (m + 2)] + ['*' + input() + '*' for _ in range(n)] + ['*' * (m + 2)]
def solve():
    p = (-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)
    q = (-1, 0), (0, -1), (0, 1), (1, 0)
    visited = [bytearray(m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i][j] == '*' and all(a[i + di][j + dj] == '*' for di, dj in p):
                for di, dj in p: visited[i + di][j + dj] = 1
            if all(a[i + di][j + dj] == '*' for di, dj in q):
                for di, dj in q: visited[i + di][j + dj] = 1
    return all(a[i][j] == '.' or visited[i][j] for i in range(1, n + 1) for j in range(1, m + 1))
print(("NO", "YES")[solve()])