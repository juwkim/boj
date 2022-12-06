N, K = map(int, input().split())
nums = map(int, input().split())
total = 0
for num in nums:
    total -= num // -2
print('YES' if total >= N else 'NO')