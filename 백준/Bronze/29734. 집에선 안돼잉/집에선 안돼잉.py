import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
T, S = g()

q, r = divmod(N, 8)
Zip = (8 * q + r) + S * (q - (r == 0))
q, r = divmod(M, 8)
Dok = (8 * q + r) + S * (q - (r == 0)) + (T + 2 * T * (q - (r == 0)))
if Zip < Dok:
    print("Zip")
else:
    print("Dok")
print(min(Zip, Dok))