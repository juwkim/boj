g = lambda: map(int, input().split()) 
N, Q = g()
nums = [int(input()) for _ in range(N)]
for _ in range(Q):
    a, b = g()
    print(sum(nums[a-1:b]))