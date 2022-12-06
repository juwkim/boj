import sys
n = int(sys.stdin.readline())
while True:
    k = int(sys.stdin.readline())
    if k == 0:
        break
    if k%n:
        print(f'{k} is NOT a multiple of {n}.')
    else:
        print(f'{k} is a multiple of {n}.')