def solve():
    N = int(input())
    M = int(input())
    a = [[*map(int, input().split())] for _ in range(N)]
    X = int(input())
    st = [(0, 0)]
    visited = [bytearray(M) for _ in range(N)]
    visited[0][0] = 1
    color = a[0][0]
    while st:
        x, y = st.pop()
        if (x, y) == (N - 1, M - 1):
            return "ALIVE"
        for i in range(max(0, x - X), min(N, x + X + 1)):
            d = X - abs(x - i)
            for j in range(max(0, y - d), min(M, y + d + 1)):
                if a[i][j] == color and not visited[i][j]:
                    visited[i][j] = 1
                    st.append((i, j))
    return "DEAD"
print(solve())