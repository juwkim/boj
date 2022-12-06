paper = [[0] * 102 for _ in range(102)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x + 1, x + 11):
        for j in range(y + 1, y + 11):
            paper[i][j] = 1

ans = sum(sum(line) for line in paper)
print(ans)