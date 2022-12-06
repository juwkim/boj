N = int(input())
buf = [input() for _ in range(N)]

ans = 0
for i in range(N):
    tmp = list(buf[i])
    for j in range(N):
        if buf[i][j] == 'Y':
            for k in range(N):
                if k != i and buf[j][k] == 'Y':
                    tmp[k] = 'Y'
    ans = max(ans, tmp.count('Y'))

print(ans)