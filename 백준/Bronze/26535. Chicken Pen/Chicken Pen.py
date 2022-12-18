from math import isqrt
N = isqrt(int(input()) - 1) + 1
print('x' * (N + 2))
for _ in range(N):
    print('x' + '.' * N + 'x')
print('x' * (N + 2))