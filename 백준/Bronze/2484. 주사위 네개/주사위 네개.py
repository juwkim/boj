def g(a, b, c, d):
    if a == b == c == d:
        return 50000 + a * 5000
    elif a == b == c or b == c == d:
        return 10000 + b * 1000
    elif a == b and c == d:
        return 2000 + (b + c) * 500
    elif a == b or b == c:
        return 1000 + b * 100
    elif c == d:
        return 1000 + c * 100
    else:
        return d * 100  
print(max(g(*sorted(map(int, input().split()))) for _ in [0]*int(input())))