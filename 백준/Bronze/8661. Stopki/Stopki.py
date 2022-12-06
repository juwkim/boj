x, k, a = map(int, input().split())
print(1 if x % (k + a) < k else 0)