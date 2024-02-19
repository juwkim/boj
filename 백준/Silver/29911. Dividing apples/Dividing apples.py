N, *apples = map(int, open(0).read().split())
l, r = 0, N - 1
a, b = 0, 0
while l <= r:
    if a < b:
        a += apples[l]
        l += 1
    else:
        b += apples[r]
        r -= 1
print(l)