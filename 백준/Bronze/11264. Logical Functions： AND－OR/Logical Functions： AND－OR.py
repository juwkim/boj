for _ in range(int(input())):
    f, w1, w2, b = input().split()
    w1, w2, b = map(float, [w1, w2, b])
    if f == 'AND' and w1 + w2 + b >= 0 and all(x < 0 for x in [w1+b, w2+b, b]):
        print('true')
    elif f == 'OR' and b < 0 and all(x >= 0 for x in [w1+b, w2+b, w1+w2+b]):
        print('true')
    else:
        print('false')