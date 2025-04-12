import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    nums = []
    for x in input().split():
        a, b = x.split('.')
        nums.append(int(a) * 1000 + int(b) * 10 ** (3 - len(b)))
    nums.sort()
    ans, Sum = "NO", nums[0]
    for i in range(1, N):
        if Sum >= nums[i]:
            ans = "YES"
            break
        Sum += nums[i]
    print(ans)