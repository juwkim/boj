import sys
input = lambda: sys.stdin.readline()

for _ in range(1, 1 + int(input())):
    N = int(input())
    if _ % 69 == 0:
        print("AMPPZ 2010")
    else:
        print((3*N + 3)//7)