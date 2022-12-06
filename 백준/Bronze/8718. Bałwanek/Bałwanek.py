x, k = map(int, input().split())
for _ in range(2):
    if 7*k > x:
        k /= 2
print(int(7000*k) if 7*k <= x else 0) 