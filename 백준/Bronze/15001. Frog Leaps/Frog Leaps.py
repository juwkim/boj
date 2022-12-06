import sys
s=[*map(int,sys.stdin.read().split()[1:])]
print(sum((x-y)**2 for x,y in zip(s,s[1:])))