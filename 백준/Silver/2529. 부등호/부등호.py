N = int(input())
arrows = input().split()
visited = [0 for _ in range(10)]
Max, Min = None, None
def solve(depth):
    global Max, Min
    if depth == N + 1:
        if Max == None or Max < nums:
            Max = nums.copy()
        if Min == None or Min > nums:
            Min = nums.copy()
        return
    
    for i in range(10):
        if visited[i] == 0 and eval(''.join([str(nums[depth-1]), arrows[depth-1], str(i)])):
            nums[depth] = i
            visited[i] = 1
            solve(depth + 1)
            visited[i] = 0
            
nums = [None for _ in range(N+1)]
for i in range(10):
    nums[0] = i
    visited[i] = 1
    solve(1)
    visited[i] = 0

print(*Max, sep='')
print(*Min, sep='')