mod = 1_000_000_007
N = int(input())
score = (N * (N + 1) * (N + 2) * (3 * N + 1) // 12) % mod
num = 1
for i in range(1, N+1):
    num = num * i * i % mod
print(score, num)