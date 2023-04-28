import datetime

while N:= int(input()):
    
    buf = []
    for _ in range(N):
        D, M, Y, C = map(int, input().split())
        buf.append((datetime.date(Y, M, D), C))
    cnt, ans = 0, 0
    for a, b in zip(buf, buf[1:]):
        if (b[0] - a[0]).days == 1:
            cnt += 1
            ans += b[1] - a[1]
    print(cnt, ans)