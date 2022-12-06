g = lambda: [*map(int, input().split())]

N = int(input())
cards = [0] + g()
dp = [0] * (1 + N)
for i in range(1, 1 + N):
    dp[i] = max(cards[j] + dp[i-j] for j in range(i+1))
print(dp[N])