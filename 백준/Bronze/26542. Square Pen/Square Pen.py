for _ in range(int(input())):
    N = int(input())
    buf = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            for size in range(1, N + 1 - max(i, j)):
                if all(buf[k][j:j + size] == '.' * size for k in range(i, i + size)):
                    ans = max(ans, size * size)
                else:
                    break
    print(ans)