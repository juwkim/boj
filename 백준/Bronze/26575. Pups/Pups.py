for _ in range(int(input())):
    d, f, p = map(float, input().split())
    print("$%.2f" % (d * f * p))