x, s = map(int, input().split())
cnt = 0
while s != 1 and x > 0:
    cnt += 1
    x -= s
    s //= 2
cnt += x * (x > 0)
print(cnt)