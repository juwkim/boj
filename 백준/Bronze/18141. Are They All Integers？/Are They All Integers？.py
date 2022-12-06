from itertools import*
input()
print('yneos'[any((x-y)%z for x,y,z in permutations(map(int,input().split()),3))::2])