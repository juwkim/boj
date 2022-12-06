from math import log
for _ in range(int(input())):
    a, b = input().split(' = ')
    s = log(float(b), 10)
    if a == 'H':
        print(f"{-s:#.2f}")
    else:
        print(f"{14 + s:#.2f}")