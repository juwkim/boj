for _ in range(int(input())):
    x = int(input())
    ans = 0
    for a in range(1, int(x**.5) + 1):
        b, q = divmod(x, a)
        if q == 0 and a / b >= 0.5:
            ans = 1
            break
    print(ans)