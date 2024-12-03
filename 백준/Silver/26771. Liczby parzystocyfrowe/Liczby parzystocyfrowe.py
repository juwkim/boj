N = int(input())
ans = []
while N:
    N, r = divmod(N, 5)
    ans.append(2 * r)
print(*ans[::-1], sep='')