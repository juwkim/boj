import sys
input = sys.stdin.readline
N, K = map(int, input().split())
S = 0
for _ in range(N):
    a = int(input())
    while a & 1 == 0:
        S += 1
        a >>= 1     
print(+(S>=K))