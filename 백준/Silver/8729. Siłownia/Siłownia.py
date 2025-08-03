import math

a, b, n = map(int, input().split())
print(n // a + n // b - n // math.lcm(a, b))