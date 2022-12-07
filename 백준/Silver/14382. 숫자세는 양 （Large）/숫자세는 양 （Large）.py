for x in range(1, 1 + int(input())):
    N = int(input())
    if N == 0:
        ans = "INSOMNIA"
    else:
        check = set()
        ans = 0
        while len(check) != 10:
            ans += N
            check.update(str(ans))
    print(f'Case #{x}: {ans}')