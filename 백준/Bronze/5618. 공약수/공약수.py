def gcd(a, b):
    if a < b: (a, b) = (b, a)
    while b != 0:
        (a, b) = (b, a % b)
    return a

n = int(input())
nums = list(map(int, input().split()))
k = nums[0]
for i in range(n-1):
    k = gcd(k, nums[i+1])

for i in range(1, k+1):
    if k % i == 0:
        print(i)