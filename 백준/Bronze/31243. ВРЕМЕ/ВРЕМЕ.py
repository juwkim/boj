import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

time = []
for _ in range(3):
    h1, m1, h2, m2 = g()
    s = ((h2 - h1) % 24) * 60 + (m2 - m1)
    time.append(s)
print("%d:%02d" % divmod(min(time), 60))
print("%d:%02d" % divmod(max(time), 60))