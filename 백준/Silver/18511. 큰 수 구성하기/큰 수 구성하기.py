from itertools import product               
N, K = input().split()
nums = input().split()
N = int(N)
ans = 0
for a in product(nums, repeat=len(str(N))):
    tmp = int(''.join(a))
    if tmp <= N:
        ans = max(ans, tmp)
if not ans:
    for a in product(nums, repeat=len(str(N))-1):
        tmp = int(''.join(a))
        if tmp <= N:
            ans = max(ans, tmp)
print(ans)