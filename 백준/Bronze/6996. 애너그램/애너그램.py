from collections import*
for _ in[0]*int(input()):
    A,B=input().split()
    S,T=map(Counter,[A,B])
    print(f'{A} & {B} are '+'NOT '*(S!=T)+'anagrams.')