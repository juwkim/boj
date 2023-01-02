def g(): return [*map(int, input().split())]

N = int(input())
Map = [g() for _ in range(N)]

if any(Map[i][i] for i in range(N)):
    ans = 1
elif any(Map[i][j] <= 0 for i in range(N) for j in range(N) if i != j):
    ans = 2
elif any(Map[i][j] != Map[j][i] for i in range(N - 1) for j in range(i + 1, N)):
    ans = 3
elif any(any(Map[i][m] + Map[m][j] < Map[i][j] for m in range(N)) for i in range(N - 1) for j in range(i + 1, N)):
    ans = 4
else:
    ans = 0
print(ans)