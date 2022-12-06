N = int(input())
M, K = map(int, input().split())
cur = M * K
nums = sorted(map(int, input().split()), reverse=True)

ans = 'STRESS'
for i in range(N):
    cur -= nums[i]
    if cur <= 0:
        ans = i + 1
        break
print(ans)