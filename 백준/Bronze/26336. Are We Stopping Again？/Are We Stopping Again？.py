import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    ans = sum(i % b == 0 or i % c == 0 for i in range(1, a))
    print(a, b, c)
    print(ans)