while m:=int(input()):
    a, b = 1, 1
    ans = 1
    while (a, b) != (0, 1):
        a, b = b, (a + b) % m
        ans += 1
    print(m, ans)