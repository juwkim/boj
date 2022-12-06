g = lambda: map(int, input().split())
for i in range(1, 1 + int(input())):
    P, K, L = g()
    nums = sorted(g(), reverse=True)
    ans = 0
    for j in range(0, len(nums), K):
        ans += (j//K + 1) * sum(nums[j:j+K])
    print(f'Case #{i}: {ans}')