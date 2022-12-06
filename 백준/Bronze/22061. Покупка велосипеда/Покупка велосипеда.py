import sys
input=sys.stdin.readline
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print('YNEOS'[a+2*min(b,c//2)<c::2])