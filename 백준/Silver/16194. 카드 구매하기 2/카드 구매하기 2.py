g = lambda: [*map(int, input().split())]

N = int(input())
cards = [0] + g()
dp = cards.copy()
for i in range(1, 1 + N):
    dp[i] = min(cards[j] + dp[i-j] for j in range(i+1))
print(dp[N])