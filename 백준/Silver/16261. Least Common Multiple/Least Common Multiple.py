from math import gcd, lcm
for t in range(int(input())):
    a, b, c, d = map(int, input().split())

    num1 = lcm(b, d)
    num2 = lcm(a * num1 // b, c * num1 // d)
    
    GCD = gcd(num1, num2)
    print(num2 // GCD, num1 // GCD)