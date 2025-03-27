n, k = map(int, input().split())
cnt = n // k
q, r = divmod(k, cnt)
print(cnt * q * (cnt * (q - 1) + 2 * r) >> 1)