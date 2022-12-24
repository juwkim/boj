h, m, s = map(int, input().split())
time = (h * 3600 + m * 60 + s + 1) % 86400
h = time // 3600
m = time % 3600 // 60
s = time % 3600 % 60
print("%02d:%02d:%02d" % (h, m, s))