import sys
input = sys.stdin.readline
t = lambda x: x * (x + 1) * (x + 2) // 6

MAX_N = 1_000_000
dp = [0] + [1e9] * MAX_N
odd_dp = [0] + [1e9] * MAX_N
tetra = [t(i) for i in range(1, 182)]; a = 0
odd_tetra = [t(i) for i in range(1, 188, 4)]; b = 0
for i in range(1, MAX_N + 1):
    if i == tetra[a]:
        a += 1
    if i == odd_tetra[b]:
        b += 1
    dp[i] = min(dp[i - tetra[k]] + 1 for k in range(a))
    odd_dp[i] = min(odd_dp[i - odd_tetra[k]] + 1 for k in range(b))

while n:=int(input()):
    print(f"{dp[n]} {odd_dp[n]}")