import sys
input = lambda: sys.stdin.readline().rstrip('\n')


g = lambda: [*map(int, input().split())]

N, M = g()
nums = [input() for _ in range(N)]
ans = 0
if N & 1:
    line = nums[N//2]
    if M & 1:
        if line[M//2] != '8':
            ans = -1
    if ans != -1:
        for i in range(M//2):
            a, b = line[i], line[M-1-i]
            if a == '8':
                if b != '8':
                    ans = -1
                    break
            elif a == '7':
                if b == '7':
                    ans += 1
                else:
                    ans = -1
                    break
            elif a == '6':
                if b == '6':
                    ans += 1
                elif b in '78':
                    ans = -1
                    break
            else:
                if b == '9':
                    ans += 1
                elif b in '78':
                    ans = -1
                    break
if ans == -1:
    print(ans)
else:
    for i in range(N//2):
        for j in range(M):
            a = nums[i][j]
            b = nums[N-1-i][M-1-j]
            if a == '8':
                if b != '8':
                    ans = -1
                    break
            elif a == '7':
                if b == '7':
                    ans += 1
                else:
                    ans = -1
                    break
            elif a == '6':
                if b == '6':
                    ans += 1
                elif b in '78':
                    ans = -1
                    break
            else:
                if b == '9':
                    ans += 1
                elif b in '78':
                    ans = -1
                    break
        if ans == -1:
            break
    print(ans)