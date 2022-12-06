import sys
print(*sorted(sys.stdin.read().split()[1:],key=int),sep='\n')