for _ in range(int(input())):
    y, m, d = map(int, input().split())
    if y < 1989 or (y == 1989 and m == 1) or (y == 1989 and m == 2 and d <= 27):
        print('Yes')
    else:
        print('No')