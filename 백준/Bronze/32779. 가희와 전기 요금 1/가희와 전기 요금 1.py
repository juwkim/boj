import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, m = map(int, input().split())
    print(a * m * 11 // 6250)