K = int(input())
dp = [0] * (K + 1)
for i in range(K, 0, -1):
    divisors = []
    for j in range(1, int(i**.5) + 1):
        if i % j == 0:
            divisors.append(j)
            if j != i // j:
                divisors.append(i // j)
    dp[i] = any(dp[i + d] == 0 for d in divisors if i + d <= K)
if dp[1]:
    print("Kali")
else:
    print("Ringo")