M, S, G = map(int, input().split())
A, B = map(float, input().split())
L, R = map(int, input().split())

a = M / S + R / B
b = M / G + L / A
print("friskus" if a > b else "latmask")