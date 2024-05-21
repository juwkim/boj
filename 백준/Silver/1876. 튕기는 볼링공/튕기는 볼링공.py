from math import radians, tan, sin, cos

for _ in range(int(input())):
    T, X = input().split()
    X = radians(int(X))
    O = 0.85 / tan(X)
    T = float(T) % O
    if abs(T * sin(X) - 0.85 * (2 * T > O) * cos(X)) <= 0.16:
        print("yes")
    else:
        print("no")