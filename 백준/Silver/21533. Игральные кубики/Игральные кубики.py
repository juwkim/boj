n = int(input())
r, q = divmod(n, 6)
if q:
    r += 7 - q
print(r, n * 6)