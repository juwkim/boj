def check(r, g, b):
    global A, C
    return A * (r**2 + g**2 + b**2) + C * min(r, g, b)


for _ in range(int(input())):
    A, C = map(int, input().split())
    r, g, b = map(int, input().split())
    check_list = [check(r + 1, g, b), check(r, g + 1, b), check(r, g, b + 1)]
    print(['RED', 'GREEN', 'BLUE'][check_list.index(max(check_list))])