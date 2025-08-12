x1, y1, x2, y2 = map(int, input().split())
L = 2024
print(bool(x1 % L or y1 % L) + bool(x2 % L or y2 % L))