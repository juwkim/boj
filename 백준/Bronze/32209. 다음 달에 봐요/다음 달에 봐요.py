import sys
input = sys.stdin.readline

ans = "See you next month"
cnt = 0
for _ in range(int(input())):
    cmd, num = map(int, input().split())
    match cmd:
        case 1:
            cnt += num
        case 2:
            cnt -= num
            if cnt < 0:
                ans = "Adios"
                break
print(ans)