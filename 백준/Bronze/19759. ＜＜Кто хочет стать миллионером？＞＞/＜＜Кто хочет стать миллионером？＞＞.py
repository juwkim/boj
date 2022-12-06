import math
def roundup(s):
    t = pow(10, (len(str(2*s)) + 1) // 2)
    return int(math.ceil(2 * s / t)) * t
s = 100
for _ in range(int(input())):
    print(s)
    s = roundup(s)