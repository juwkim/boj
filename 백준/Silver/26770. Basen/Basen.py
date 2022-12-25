N = int(input())
ans, d = 1, 0
prev = 0
for num in map(int, input().split()):
    if d == 0:
        if num < prev:
            d = 1
            ans += 1
    else:
        if num > prev:
            d = 0
            ans += 1
    prev = num
print(ans)