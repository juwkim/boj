while True:
    a, b, c, d = map(int, input().split())
    if (a, b, c, d) == (0, 0, 0, 0):
        break
    count = 0
    while True:
        if a==b==c==d:
            break
        a, b, c, d = map(abs, [a-b, b-c, c-d, d-a])
        count += 1
    print(count)