from math import sin, tan, radians

for _ in range(int(input())):
    T, X = input().split()
    T, X = float(T), radians(int(X))
    one_step = 0.85 / tan(X)
    T %= one_step
    d = min(T, one_step - T) * sin(X)
    print('yes' if d <= 0.16 else 'no')