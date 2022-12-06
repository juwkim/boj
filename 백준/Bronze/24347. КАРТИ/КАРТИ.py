from itertools import*
print(max(map(''.join,permutations(input().split(),4)),key=int))