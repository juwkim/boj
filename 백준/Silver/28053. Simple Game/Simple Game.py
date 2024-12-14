from math import gcd

n, a, b = map(int, input().split())
if gcd(a, b) == 1:
    print("Yes")
    for i in range(0, 2 * n, 2):
        print(a + i * b, a + (i + 1) * b)
else:
    print("No")