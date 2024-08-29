import sys
input = sys.stdin.readline

ans = 0
for _ in range(int(input())):
    A, B = map(int, input().split())
    ans += A - B
    print(ans)