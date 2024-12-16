import sys
input = sys.stdin.readline

n = int(input())
x, y = zip(*[[*map(int, input().split())] for _ in range(n)])
print(sorted(x)[n-1>>1], sorted(y)[n-1>>1])