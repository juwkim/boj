l, h = map(int, input().split())
print(h - (h & 1) * (l % 2 == 0))