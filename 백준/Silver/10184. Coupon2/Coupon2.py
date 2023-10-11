import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    X, Y = g()
    dic = {}
    for _ in range(X):
        s, p = input().split()
        dic[s] = float(p)
    invalid = []
    for _ in range(Y):
        s, p = input().split()
        if s in dic:
            dic[s] *= (1 - float(p))
        else:
            invalid.append(s)
    print("%.2f" % sum(dic.values()))
    if invalid:
        print("INVALID COUPONS")
        for coupon in invalid:
            print(coupon)