for _ in range(int(input())):
    n = int(input())
    print(n, sum([n % i == 0 for i in range(1, n+1)]))