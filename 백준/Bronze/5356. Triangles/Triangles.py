for _ in range(int(input())):
    N, C = input().split()
    for i in range(1, int(N) + 1):
        print(C * i)
        C = chr(65 + (ord(C) - 64) % 26)
    print()