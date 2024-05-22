from math import comb, factorial

N = int(input())
t = N >> 1
ans = 1
for i in range(N, 1, -2):
    ans *= comb(i, 2)
print(ans // factorial(t))