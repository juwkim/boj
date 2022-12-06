import math
for _ in range(int(input())):
    y, n = input().split()
    print(str(math.factorial(int(y))).count(n))