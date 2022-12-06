import sys
input = lambda: sys.stdin.readline().rstrip('\n')

for _ in range(int(input())):
    N = int(input())
    ans = 0
    num = 0
    for _ in range(N):
        num += int(input())
        if num < 0:
            num += 1
            ans += 1
    print(abs(num) + ans)