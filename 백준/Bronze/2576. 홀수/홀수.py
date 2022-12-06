import sys
num = [n for n in map(int, sys.stdin.read().split()) if n % 2]
if num:
    print(sum(num), min(num), sep='\n')
else:
    print(-1)