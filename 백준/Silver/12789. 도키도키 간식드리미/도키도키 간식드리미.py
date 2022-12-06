g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
idx = 0
stack = []
ans = 'Nice'
for cur in range(1, 1 + N):
    if stack and stack[-1] == cur:
        stack.pop()
    elif idx == N:
        ans = 'Sad'
        break
    else:
        while idx < N and nums[idx] != cur:
            stack.append(nums[idx])
            idx += 1
        if idx == N:
            ans = 'Sad'
            break
        idx += 1
print(ans)