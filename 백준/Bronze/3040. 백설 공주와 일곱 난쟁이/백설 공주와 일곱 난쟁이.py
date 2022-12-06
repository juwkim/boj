from itertools import*
for n in combinations([int(input())for _ in[0]*9],7):
    if sum(n)==100:
        print(*n)
        break