import sys
input = sys.stdin.readline

a = [0] * 86400
for _ in range(int(input())):
    M, *nums = map(int, input().split())
    for i in range(0, 2 * M, 2):
        L, R = nums[i], nums[i + 1]
        for j in range(L, R + 1):
            a[j] += 1
Max = max(a)
print(Max)
print(a.count(Max))