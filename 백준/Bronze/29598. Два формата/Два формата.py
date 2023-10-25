import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
buf = []
while n:
    n, r = divmod(n, 256)
    buf.append(r)
M = 0
for num in buf:
    M = (M << 8) | num
print(M)