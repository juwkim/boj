h, m, s = map(int, input().split())
t = (h * 3600 + m * 60 + s + int(input())) % 86400
print(t // 3600, (t % 3600) // 60, t % 60)
