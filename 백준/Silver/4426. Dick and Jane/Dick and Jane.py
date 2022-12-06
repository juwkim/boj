def solve():
    for yertle in range(13 + j):
        for a, b in product((y, y + 1), (p, p + 1)):
            if a - b in (s, s + 1):
                spot = yertle + a
                puff = yertle + b
                if spot + puff + yertle == 12 + j:
                    print(spot, puff, yertle)
                    return
    
from itertools import product
while True:
    try:
        s, p, y, j = map(int, input().split())
        solve()
    except:
        break