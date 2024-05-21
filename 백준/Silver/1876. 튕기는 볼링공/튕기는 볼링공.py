from math import sin, tan, radians

for _ in range(int(input())):
    T, X = input().split()
    T, X = float(T), radians(int(X))
    one_step = 0.85 / tan(X)
    while T >= one_step:
        T -= one_step
    if 2 * T > one_step:
        T = one_step - T
    d = T * sin(X)
    if d <= 0.16:
        print('yes')
    else:
        print('no')