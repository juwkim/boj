import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

T = int(input())
x = [int(input()) for _ in range(T)]
a, b = 0, 0
while a <= 10000:
    b = 0
    while b <= 10000:
        if all((x[i+1] - a * a * x[i] - a * b - b) % 10001 == 0 for i in range(T - 1)):
            break
        b += 1
    else:
        a += 1
        continue
    break
for num in x:
    print((a * num + b) % 10001)