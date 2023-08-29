import sys
input = sys.stdin.readline

from decimal import Decimal, getcontext

getcontext().prec = 30
for _ in range(int(input())):
    A, B, C, D = map(int, input().split())
    
    L = Decimal(A) + Decimal(B).sqrt()
    R = Decimal(C) + Decimal(D).sqrt()
    
    if L < R:
        print("Less")
    elif L > R:
        print("Greater")
    else:
        print("Equal")