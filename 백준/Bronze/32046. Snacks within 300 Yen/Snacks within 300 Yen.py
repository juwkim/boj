import sys
input = sys.stdin.readline

while int(input()):
    ans = 0
    for num in map(int, input().split()):
        if ans + num <= 300:
            ans += num
    print(ans)