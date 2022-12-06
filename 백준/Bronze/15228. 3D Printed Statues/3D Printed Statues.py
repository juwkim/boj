n = int(input())
a, cnt = 1, 1
while a < n:
    a <<= 1
    cnt += 1
print(cnt)