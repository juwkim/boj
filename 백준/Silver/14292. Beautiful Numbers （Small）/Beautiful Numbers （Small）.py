from math import log
for case in range(1, 1 + int(input())):
    
    n = int(input())
    base = 2
    while True:
        tmp = log(n * (base - 1) + 1, base)
        if tmp % 1 == 0:
            break
        base += 1
    print(f'Case #{case}: {base}')