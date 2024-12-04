g, r = map(int, input().split())
a, b = divmod(max(0, g - r), 3)
print((a + min(g, r)) * 10 + (0, 1, 3)[b])