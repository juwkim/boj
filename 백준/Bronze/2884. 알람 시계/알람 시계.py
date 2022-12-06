import sys

H, M = map(int, sys.stdin.readline().split())

minutes = H * 60 + M - 45

if minutes < 0:
    print("23 %d" % (60 + minutes))
elif minutes == 0:
    print("0 0")
else:
    print("%d %d" % (minutes // 60, minutes % 60))