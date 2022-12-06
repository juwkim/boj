N, C = map(int, input().split())
s, t = N, N
for _ in range(C):
    X, Y = map(int, input().split())
    if X < s and Y < t:
        if Y * s > X * t: t = Y
        else: s = X
print(s * t)