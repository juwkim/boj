N = int(input())
if N&1:
    cur = (N + 1) // 2
    while cur != 1:
        print(cur, cur + N // 2, end=' ')
        cur -= 1
    print(cur)
else:
    cur = N // 2
    while cur != 0:
        print(cur, cur + N // 2, end=' ')
        cur -= 1