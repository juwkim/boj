for _ in range(int(input())):
    q, r = divmod(int(input()), 2)
    if r == 0:
        ans = '1' * (2 * q)
    elif q & 1:
        ans = '1' * q + '2' + '1' * q
    else:
        ans = '1' * q + '0' + '1' * q
    print(ans)