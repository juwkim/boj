import sys
input = sys.stdin.readline

while True:
    K, R = input().split()
    if K == '0':
        break
    K, R = int(K), float(R)
    nums = []
    for _ in range(int(K)):
        N, M = map(int, input().split())
        nums.append(N)
    nums.sort()
    ans, Min = 1, nums[0]
    for i in range(1, K):
        if nums[i] > Min * R:
            ans += 1
            Min = nums[i]
    print(ans)