import sys
input = sys.stdin.readline

ans = []
for i in range(1, int(input()) + 1):
    s, x = input().split()
    if s[0] == 'T' and (len(ans) < 10 or int(x) < 2):
        ans.append(i)
        if len(ans) == 20:
            break
print(*ans)