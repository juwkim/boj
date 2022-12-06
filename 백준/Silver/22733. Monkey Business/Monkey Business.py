from math import isqrt
while N:= int(input()):
    for i in range(1, 1 + isqrt(N)):
        print(i * i)
    print()