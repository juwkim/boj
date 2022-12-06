h, m = map(int, input().split())
t = (h * 60 + m + int(input())) % 1440
print(t // 60, t % 60)
