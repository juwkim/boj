import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(min(n, k-1))