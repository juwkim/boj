n = int(input())
l, r, *nums = map(int, input().split())
for num in nums:
    if l > r:
        r += num
    else:
        l += num
diff = abs(l - r)
ans = 0
for chu in (100, 50, 20, 10, 5, 2, 1):
    q, diff = divmod(diff, chu)
    ans += q
print(ans)