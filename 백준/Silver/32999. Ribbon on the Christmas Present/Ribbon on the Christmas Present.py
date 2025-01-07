n, *d = map(int, open(0).read().split())
ans, nums = 0, sorted({*d})
for num in nums:
    new = True
    for color in d:
        if color < num:
            new = True
        elif color == num and new:
            new = False
            ans += 1
print(ans)