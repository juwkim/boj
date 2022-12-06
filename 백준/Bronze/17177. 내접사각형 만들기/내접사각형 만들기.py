a, b, c = map(int, input().split())
if a**2 <= b**2 + c**2:
    print(-1)
else:
    print(round(((a**2 - c**2)**.5 * (a**2 - b**2)**.5 - b * c) / a))