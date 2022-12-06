for _ in range(int(input())):
    N = input()
    l = len(N)
    N = min(int(N), int('4' + '9' * (l - 1)))
    print(N * (int('9' * l) - N))