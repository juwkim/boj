import sys
input = sys.stdin.readline
for _ in range(int(input())):
    p, n = map(int, input().split())
    print(bin(p-1).count('1') % n)