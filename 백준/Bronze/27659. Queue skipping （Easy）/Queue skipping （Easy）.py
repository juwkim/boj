for _ in range(int(input())):
    input()
    n, e = map(int, input().split())
    buf = [int(input()) for _ in range(e)]
    check = set(range(1, n + 1))
    for i in range(e - 1, -1, -1):
        if len(check) == 1:
            break
        if buf[i] in check:
            check.remove(buf[i])
    print(max(check))