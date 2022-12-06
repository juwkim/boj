while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (0, 0, 0):
        break
    if b > a//2:
        print(0)
    else:
        print(a//2 + 1 - b if a//2 + c < a else -1)