N, *A = map(int, open(0).read().split())
t = 0
for num in A:
    t ^= num
ans = t
for num in A:
    ans = max(ans, t ^ num)
print(ans, ans, sep='')