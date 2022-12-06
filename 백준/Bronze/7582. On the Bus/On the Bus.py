while (s:=input()) != '# 0':
    route_num, Z = s.split()
    Z, P = map(int, [Z, input()])
    for _ in range(int(input())):
        Out, In = map(int, input().split())
        P = min(Z, P - Out + In)
    print(route_num, P)