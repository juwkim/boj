for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print(['Imp','P'][a in [b+c,b-c,c-b,b*c,b/c,c/b]]+'ossible')