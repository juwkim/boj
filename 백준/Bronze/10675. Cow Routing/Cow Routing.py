A, B, N = map(int, input().split())
min_price = 10000
for _ in range(N):
    p = int(input().split()[0])
    air = [*map(int, input().split())]
    try:
        if air.index(A) < air.index(B) and p < min_price:
            min_price = p
    except:
        pass
print(min_price if min_price != 10000 else -1)