import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    N = int(input())
    nums = g()
    diff = [nums[i] - nums[i+1] for i in range(N-1)]
    
    ans, tmp = 2, 2
    for i in range(N-2):
        if diff[i] == diff[i+1]:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 2
    ans = max(ans, tmp)
    print(f'Case #{cnt}: {ans}')