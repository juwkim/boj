R, B = map(int, input().split())
s, t = 1 + R / 4, ((R/4 - 1)**2 - B)**.5
print(*map(round, [s+t, s-t]))