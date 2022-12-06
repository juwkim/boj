import sys
import math
T = int(input())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    k = math.ceil(math.sqrt(distance) - 1)
    print(2 * k if distance <= k * (k + 1) else 2 * k + 1)