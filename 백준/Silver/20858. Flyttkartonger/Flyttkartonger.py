N = int(input())
a = [*map(int, input().split())]
ans = 0
for i in range(N - 2, -1, -1):
    ans = max(0, 2 * ans + a[i + 1] - a[i])
print(ans)