for _ in range(int(input())):
    n = int(input())
    k = [0]*(n+1)
    for i in range(1, n+1):
        j = 1
        while i * j <= n:
            k[i * j] = (k[i * j] + 1) % 2
            j += 1
    print(k.count(1))