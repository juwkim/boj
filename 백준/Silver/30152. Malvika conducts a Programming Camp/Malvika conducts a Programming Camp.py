for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 1:   print(0)
    elif n == 2: print(m)
    else:        print(n + 2 * m - 3)