g = lambda: [*map(int, input().split())]

while True:
    try:
        s = [1] + g() + [1]
        for i in range(1, len(s) - 1):
            print(s[i-1] * s[i] * s[i+1], end=' ')
        print()
    except:
        break