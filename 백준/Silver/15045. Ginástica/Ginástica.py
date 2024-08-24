T, M, N = map(int, input().split())
s = [0] + [1] * (N - M + 1) + [0]
for _ in range(T - 1):
    s = [0] + [(s[i - 1] + s[i + 1]) % 1000000007 for i in range(1, N - M + 2)] + [0]
print(sum(s) % 1000000007)