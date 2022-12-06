for i in range(1, 1 + int(input())):
    a, b, cnt = 1, 1, 0
    m = int(input().split()[1])
    while True:
        a, b = b, (a + b) % m
        cnt += 1
        if a == 1 and b == 1:
            break
    print(i, cnt)