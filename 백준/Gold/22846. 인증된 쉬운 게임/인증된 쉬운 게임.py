def divisors(n):
    div = []
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n // i)
    return div

K = int(input())
dp = [0] * (K + 1)
for i in range(K, 0, -1):
    dp[i] = any(dp[i + d] == 0 for d in divisors(i) if i + d <= K)
print(("Ringo", "Kali")[dp[1]])