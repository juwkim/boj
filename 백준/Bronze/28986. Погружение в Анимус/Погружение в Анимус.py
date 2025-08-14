n, k = map(int, input().split())
print(max(0, min(n, k - 1 >> 1) - max(k - n, 1) + 1))