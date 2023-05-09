N, H, W = map(int, input().split())
for _ in range(N):
    a, b = input().split()
    ans = []
    if a == 'Y' or W == 0:
        H -= 1
        W += 1
        ans.append('Y')
    else:
        ans.append('N')

    if b == 'Y' or H == 0:
        W -= 1
        H += 1
        ans.append('Y')
    else:
        ans.append('N')
    print(*ans)