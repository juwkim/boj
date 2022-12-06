for _ in range(int(input())):
    m, n = map(int, input().split())
    a = [*map(int, input().split())]
    left = (3 in a)
    cur = a.index(2 + left)
    
    cnt = 0
    while n:
        if cur == 0:
            left = 0
        elif cur == m - 1:
            left = 1
        cur += 1 - 2 * left
        cnt += (a[cur] == 0)
        n -= 1
    print(cnt)