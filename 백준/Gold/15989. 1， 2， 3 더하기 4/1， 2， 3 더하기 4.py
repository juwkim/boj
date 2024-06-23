import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    print(sum(1 + (n - 3 * i) // 2 for i in range(n // 3 + 1)))