a1, a0 = map(int, input().split())
C = int(input())
n0 = int(input())
print(int(C <= a1 and (a1 - C) * n0 + a0 >= 0))