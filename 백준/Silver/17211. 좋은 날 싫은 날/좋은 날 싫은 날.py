N, S = map(int, input().split())
a, b, c, d = map(float, input().split())
for _ in range(N):
    S = S * d + (1 - S) * b
S *= 1000
print(round(1000 - S), round(S))