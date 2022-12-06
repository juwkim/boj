a, b, c = map(int, input().split())
res = 1
while b > 0:
    if b % 2:
        res = res * a % c
    a = a**2 % c
    b //= 2
print(res)