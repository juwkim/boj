import sys
input=sys.stdin.readline
for _ in range(int(input())):P=int((N:=int(input()))**.5);print((N+P*P+P-1)//P*2)