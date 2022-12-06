import sys
for _ in [0]*int(input()):
    n = int(sys.stdin.readline())
    array = [n]
    while n - 1:
        if n % 2:
            n = 3*n + 1
        else:
            n //= 2
        array += [n]
    print(max(array))