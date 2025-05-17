import math

def is_square(x):
    return math.isqrt(x) ** 2 == x

cnt = 0
double_S = 2 * int(input())
for a in range(1, math.isqrt(double_S) + 1):
    b, r = divmod(double_S, a)
    if r == 0:
        x = a * a + b * b
        cnt += math.isqrt(x) ** 2 == x
print(cnt)