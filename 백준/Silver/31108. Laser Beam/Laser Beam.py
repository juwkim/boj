a, b = map(int, input().split())
cnt = 0
while a + b < 180:
    b += a
    cnt += 1
print(cnt)