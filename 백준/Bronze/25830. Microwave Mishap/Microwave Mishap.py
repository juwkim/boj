h, m = map(int, input().split(':'))
t = h * 3600 + m * 60 - (h * 60 + m)
t, s = divmod(t, 60)
h, m = divmod(t, 60)
print("%02d:%02d:%02d" % (h, m, s))