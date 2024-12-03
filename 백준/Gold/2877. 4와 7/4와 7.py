N = int(input()) - 1
d, l = 2, 1
while N >= d:
    N -= d
    d <<= 1
    l += 1
ans = []
for _ in range(l):
    N, r = divmod(N, 2)
    ans.append((4, 7)[r])
print(*ans[::-1], sep='')