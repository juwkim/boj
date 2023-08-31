N, a, b = map(int, input().split())
ans = 0
for _ in range(N):
    cnt, *nums = map(int, input().split())
    for num in nums:
        bi = bin(num)[2:]
        ans += a * bi.count('0') + b * bi.count('1')
print(ans)