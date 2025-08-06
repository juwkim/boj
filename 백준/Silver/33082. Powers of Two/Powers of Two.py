import sys
input = sys.stdin.readline

N = 0
for _ in range(int(input())):
    T, x = input().split()
    num = 1 << int(x)
    if T == '+':
        N += num
    else:
        N -= num
    if N:
        print("NO")
    else:
        print("YES")