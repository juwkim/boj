for _ in range(int(input())):
    a, b = map(int, input().split())
    print(''.join(map(lambda s: chr((a * (ord(s)-65) + b) % 26 + 65), input())))