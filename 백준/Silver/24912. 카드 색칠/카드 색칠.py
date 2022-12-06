import sys
input = lambda: sys.stdin.readline().rstrip('\n')

N = int(input())
if N == 1:
    print(1)
else:
    nums = [*map(int, input().split())]
    ans = 0
    for i in range(N):
        if i == 0:
            a = nums[i]
            b = nums[i+1]
            if a:
                if a == b:
                    ans = -1
                    break
            else:
                nums[i] = [3, 2, 1, 1][b]
        elif i == N - 1:
            a = nums[i]
            if a == 0:
                b = nums[i-1]
                nums[i] = [3, 2, 1, 1][b]
        else:
            a = nums[i]
            b = nums[i-1]
            c = nums[i+1]
            if a == 0:
                
                check = set([1, 2, 3])
                check.remove(b)
                if c == 0:
                    nums[i] = check.pop()
                else:
                    if c in check:
                        check.remove(c)
                    nums[i] = check.pop()
            elif a == c:
                ans = -1
                break
                
    if ans == -1:
        print(ans)
    else:
        print(*nums)