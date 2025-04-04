g = lambda: [*map(int, input().split())]

def solve():
    N, M, K = g()
    a = [g() for _ in range(N)]
    if M == 0 or all(all(l) for l in a):
        return "IMPOSSIBLE"
    for i in range(N):
        for j in range(N):
            if a[i][j]:
                continue
            a[i][j] = 1
            st, cnt = [(i, j)], 1
            while st:
                x, y = st.pop()
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N and not a[nx][ny]:
                        a[nx][ny] = 1
                        cnt += 1
                        st.append((nx, ny))
            M -= (cnt + K - 1) // K
            if M < 0:
                return "IMPOSSIBLE"
    return f"POSSIBLE\n{M}"

print(solve())