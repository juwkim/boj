g = lambda: [*map(int, input().split())]

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime

n, a, b = g()
row1 = g()
row2 = g()
is_prime = sieve(200000)
dp = [0] * (n + 1)
dp[1] = (b, a)[is_prime[row1[0] + row2[0]]]
for i in range(2, n + 1):
    dp[i] = max(dp[i - 1] + (b, a)[is_prime[row1[i - 1] + row2[i - 1]]], dp[i - 2] + (b, a)[is_prime[row1[i - 1] + row1[i - 2]]] + (b, a)[is_prime[row2[i - 2] + row2[i - 1]]])
print(dp[n])