from math import gcd

a = [0, 3]
for i in range(2, 1001):
    a.append(a[i - 1] + 2 * sum(gcd(i, j) == 1 for j in range(1, i)))

for _ in range(int(input())):
    print(a[int(input())])