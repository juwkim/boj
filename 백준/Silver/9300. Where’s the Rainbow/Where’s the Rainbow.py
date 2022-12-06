from math import tan, radians
for _ in range(1, 1 + int(input())):
    h, theta = map(float, input().split())
    if theta:
        ans = abs(h / tan(radians(theta)) - h)
    else:
        ans = 'Infinity'
    print(f'Case {_}: {ans}')