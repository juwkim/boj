for _ in range(int(input())):
    n, s = input().split()
    n = int(n)
    print(s[:n-1]+s[n:])