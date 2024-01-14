import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K, A, B = g()
cnt = (N + A - 1) // A
day = 1
water = K
while water:
    if day % cnt == 0:
        water += B
    water -= 1
    day += 1
print(day - 1)