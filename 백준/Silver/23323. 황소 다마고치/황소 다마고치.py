import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(len(bin(n)) + m - 2)