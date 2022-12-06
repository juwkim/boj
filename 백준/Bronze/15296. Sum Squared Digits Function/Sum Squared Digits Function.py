for _ in range(int(input())):
    K, b, n = map(int, input().split())
    total = 0
    while n:
        total += (n%b)**2
        n //= b
    print(K, total)