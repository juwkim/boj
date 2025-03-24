T, H = map(int, input().split())
if H > 2 * T:
    print((2 * T * H) ** .5)
else:
    print(T + H / 2)