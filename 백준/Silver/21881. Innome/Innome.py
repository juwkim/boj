import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m, k = map(int, input().split())
    i = int((2 * m / k + .25)**.5 - .5)
    print(k * i + (m - i * (i + 1) * k // 2) // (i + 1))