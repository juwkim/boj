from math import pi, sqrt
for _ in range(int(input())):
    l, r = map(int, input().split())
    area = pi * r * sqrt(r * r - l * l) / 4
    q, r = divmod(area, 100)
    ans = (q + (r >= 50)) * 100
    print(ans)