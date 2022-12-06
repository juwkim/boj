while True:
    start, end = 1, 50
    n = int(input())
    if n == 0:
        break
    while True:
        now = (start + end)//2
        print(now, end=' ')
        if now == n:
            break
        if now < n:
            start = now + 1
        else:
            end = now - 1