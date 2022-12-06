for _ in range(int(input())):
    n, m = map(int, input().split())
    count = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            k = (a**2 + b**2 + m)/(a*b)
            if k == int(k):
                count += 1
    print(count)