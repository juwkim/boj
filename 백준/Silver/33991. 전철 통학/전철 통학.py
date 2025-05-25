import sys
input = sys.stdin.readline

X1, Y1, X2, Y2, X3, Y3 = map(int, input().split())
for _ in range(int(input())):
    X, Y, T1, T2, T3 = map(int, input().split())
    a = abs(X - X1) + abs(Y - Y1)
    a += T1 - (a - 1) % T1 - 1
    b = abs(X - X2) + abs(Y - Y2)
    b += T2 - (b - 1) % T2 - 1
    c = abs(X - X3) + abs(Y - Y3)
    c += T3 - (c - 1) % T3 - 1
    print(min(a, b, c))