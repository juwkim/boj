N = int(input())
M = int(input())
x = [*map(int, input().split())]
ans = max(x[0], N - x[-1])
for i in range(M - 1):
    ans = max(ans, (x[i+1] - x[i] + 1) // 2)
print(ans)