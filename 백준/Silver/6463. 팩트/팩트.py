import math
while True:
    try:
        N = int(input())
        a = str(math.factorial(N)).rstrip('0')[-1]
        print(f'{N:5d} -> {a}')
    except:
        break