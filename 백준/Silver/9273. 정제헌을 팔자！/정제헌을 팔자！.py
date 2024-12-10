for s in open(0):
    n = int(s.split('/')[1])
    print(sum(n * n % i == 0 for i in range(1, n + 1)))