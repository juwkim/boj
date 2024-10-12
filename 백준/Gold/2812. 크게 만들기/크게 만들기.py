N, K = map(int, input().split())
ans = []
for c in input():
    while K and ans and ans[-1] < c:
        ans.pop()
        K -= 1
    ans.append(c)
print(*ans[:len(ans)-K], sep='')