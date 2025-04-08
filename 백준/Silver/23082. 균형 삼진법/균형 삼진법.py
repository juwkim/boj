N = int(input())
ans = []
while True:
    N, r = divmod(N, 3)
    if r == 2:
        ans.append('T')
        N += 1
    else:
        ans.append(str(r))
    if N == 0:
        break
print(*ans[::-1], sep='')