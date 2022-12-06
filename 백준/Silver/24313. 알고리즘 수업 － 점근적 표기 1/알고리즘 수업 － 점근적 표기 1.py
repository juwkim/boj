a1, a0 = map(int, input().split())
C = int(input())
n0 = int(input())
print(int(C >= a1 and (C - a1) * n0 >= a0))