for _ in range(int(input())):
    n, *l = map(int, input().split())
    print(['yes', 'no'][all(l[2*i] + l[2*i+1] == n for i in range(n))])