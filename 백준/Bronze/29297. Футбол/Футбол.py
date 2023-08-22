for _ in range(int(input())):
    s, t = map(int, input().split(':'))
    a, b = 0, 0
    for i in range(10):
        for j in range(10):
            if s + i > t + j:
                a += 1
            elif s + i < t + j:
                b += 1
            elif i > t:
                a += 1
            elif i < t:
                b += 1
    print(a, b)