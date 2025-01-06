import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    nums = [[*map(int, input().split())] for _ in range(x)]
    day = int(input())
    ans = 0
    for l in nums:
        *step, last = l
        if last == -1:
            ans += sum(step) == day
        else:
            num = day - sum(step[i] for i in range(last))
            ans += num > 0 and num % sum(step[last:]) == 0
    print(ans)