import sys
a=[*map(int,sys.stdin.read().split())]
print(sum(a[1:])+1-a[0])