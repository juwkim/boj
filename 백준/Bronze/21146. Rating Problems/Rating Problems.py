n, k = map(int, input().split())
s = 3 * (n - k)
score = sum(int(input()) for _ in range(k))
print((score - s) / n, (score + s) / n)