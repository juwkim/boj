N = int(input())
nums = sorted(map(int, input().split()))
ticket = N + 1
for i in range(N):
    if nums[i] != i + 1:
        ticket = i + 1
        break
print(ticket)