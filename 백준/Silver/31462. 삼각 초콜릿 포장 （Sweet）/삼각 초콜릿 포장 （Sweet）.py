import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ans = 1
if N % 3 == 1:
    ans = 0
else:
    visited = [bytearray(i + 1) for i in range(N)]
    l = [input() for _ in range(N)]
    for i in range(N):
        for j in range(i + 1):
            if visited[i][j]:
                continue
            if l[i][j] == 'R':
                if i < N - 1 and not visited[i + 1][j] and not visited[i + 1][j + 1] and l[i + 1][j] == 'R' and l[i + 1][j + 1] == 'R':
                    visited[i][j] = True
                    visited[i + 1][j] = True
                    visited[i + 1][j + 1] = True
                else:
                    ans = 0
                    break
            else:
                if i < N - 1 and j < i and not visited[i][j + 1] and not visited[i][j + 1] and l[i + 1][j + 1] == 'B' and l[i + 1][j + 1] == 'B':
                    visited[i][j] = True
                    visited[i][j + 1] = True
                    visited[i + 1][j + 1] = True
                else:
                    ans = 0
                    break
        else:
            continue
        break
print(ans)