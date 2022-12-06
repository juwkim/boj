import sys

while(True):
    A, B, C = sorted(list(map(int, sys.stdin.readline().split())))
    if not A:
        break
    if A**2 + B**2 == C**2:
        print("right")
    else:
        print("wrong")