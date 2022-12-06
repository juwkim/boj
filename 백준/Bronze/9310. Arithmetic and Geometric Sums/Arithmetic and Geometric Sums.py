while True:
    n = int(input())
    if n == 0:
        break
    a, b, c = map(int, input().split())
    if a + c == 2*b:
        print(n*(2*a+(n-1)*(b-a))//2)
    else:
        print(a*((b//a)**n - 1)//(b//a - 1))