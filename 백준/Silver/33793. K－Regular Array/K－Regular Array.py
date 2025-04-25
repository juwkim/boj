import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    print(*[(k - i - 1) % k + 1 for i in range(n)])