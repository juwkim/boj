import math
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    s = 225 - (a * 15 + b * 20 + c * 25) / 40
    if s <= 100:
        print(math.ceil(s))
    else:
        print('impossible')