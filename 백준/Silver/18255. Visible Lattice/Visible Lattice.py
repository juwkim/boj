import math

for _ in range(int(input())):
    N = int(input())
    print(sum(math.gcd(x, y, z) == 1 for x in range(N + 1) for y in range(N + 1) for z in range(N + 1)))