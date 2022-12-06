paper = [[0] * 102 for _ in range(102)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x + 1, x + 11):
        for j in range(y + 1, y + 11):
            paper[i][j] = 1

ans = sum(sum(x + y == 1 for x, y in zip(line, line[1:])) for line in paper)

for j in range(1, 101):
    for i in range(101):
        ans += paper[i][j] != paper[i+1][j]

print(ans)