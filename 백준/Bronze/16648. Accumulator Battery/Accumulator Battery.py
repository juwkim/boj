t, p = map(int, input().split())
print(t * min(2 * p, p + 20) / max(100 - p, 120 - 2 * p))