N, M = map(int, input().split())
hh, mm = divmod(1440 * M / N, 60)
print("%02d:%02d" % (hh, mm))