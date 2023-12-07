import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

H, M = map(int, input().split(":"))
N = int(input())
t = H * 60 + M
if t % 15:
    t += (15 - t % 15)

while True:
    if t % 60 == 0:
        cnt = (t // 60 - 1) % 12 + 1
        N -= cnt
    else:
        N -= 1
    if N <= 0:
        break
    t += 15

h, m = divmod(t, 60)
h = (h - 1) % 12 + 1
print(f"{h:02d}:{m:02d}")