g = lambda: [*map(int, input().split())]

from math import comb
for _ in range(int(input())):
    N, V1, V2, W = g()
    num = N - V1 - V2
    
    p = 0
    for i in range(max(0, (V2-V1+num)//2+1), num+1):
        p += comb(num, i)
    p *= 100 / pow(2, num)
    if p > W:
        print('GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!')
    elif p == 0:
        print('RECOUNT!')
    else:
        print('PATIENCE, EVERYONE!')