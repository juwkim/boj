import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    nums = sorted(map(float, input().split()))
    ans, Sum = "NO", nums[0]
    for i in range(1, N):
        if Sum >= nums[i]:
            ans = "YES"
            break
        Sum += nums[i]
    print(ans)