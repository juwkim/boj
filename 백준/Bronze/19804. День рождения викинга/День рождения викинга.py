import math
R, L = map(float, input().split())
L = min(L/2, R)
y = math.sqrt(R*R - L*L)
print(-L, y)
print(L, y)