g = lambda: list(map(int, input().split()))
N, M = g()
box = [g() for _ in range(N)]
ans = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        num = min(box[i][j-1:j+2] + box[i-1][j:j+1] + box[i+1][j:j+1])
        if num == box[i][j]:
            num -= 1
        ans += max(0, num)
print(ans)