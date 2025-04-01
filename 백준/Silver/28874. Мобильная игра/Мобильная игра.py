import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if (a - b) % 3 and (b - c) % 3 and (c - a) % 3:
        ans = "No"
    else:
        ans = "Yes"
    print(ans)