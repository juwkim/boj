import sys
input = sys.stdin.readline

MAX_N = 1_000_000
dp = [0] + [1e9] * MAX_N
odd_dp = [0] + [1e9] * MAX_N
tetra = []; a = 1
odd_tetra = []; b = 1
for i in range(1, MAX_N + 1):
    if i == a * (a + 1) * (a + 2) // 6:
        tetra.append(a * (a + 1) * (a + 2) // 6)
        a += 1
    if i == b * (b + 1) * (b + 2) // 6:
        odd_tetra.append(b * (b + 1) * (b + 2) // 6)
        b += 4        
    dp[i] = min(dp[i - num] + 1 for num in tetra)
    odd_dp[i] = min(odd_dp[i - num] + 1 for num in odd_tetra)

while n:=int(input()):
    print(f"{dp[n]} {odd_dp[n]}")