import sys
input = sys.stdin.readline

check = bytearray(360)
for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(180 + a - b, 180 + a + b + 1):
        check[i % 360] = 1
print(sum(check))