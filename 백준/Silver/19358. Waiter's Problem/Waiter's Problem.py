import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    ans = 0
    i = 0
    for x in sorted(map(int, input().split()), reverse=True):
        if x <= i:
            continue
        ans += x - i
        i += 1
    print(ans)