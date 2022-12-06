from math import factorial
for _ in range(int(input())):
    print((factorial(int(input())) - 1) % (10**9 + 7))