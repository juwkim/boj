C = float(input())
S = 0
for _ in range(int(input())):
    W, I = map(float, input().split())
    S += W * I
print(S * C)