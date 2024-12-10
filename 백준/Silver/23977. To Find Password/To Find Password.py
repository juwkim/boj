from math import lcm

K, N, *A = map(int, open(0).read().split())
print(lcm(*A) - K)