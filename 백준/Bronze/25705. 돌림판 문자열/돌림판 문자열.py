N = int(input())
pan = input()
M = int(input())

ans, cur = 0, N - 1
for c in input():
    flag = False
    for i in range(N):
        cur = (cur + 1) % N
        ans += 1
        if pan[cur] == c:
            flag = True
            break
    if flag == False:
        ans = -1
        break
print(ans)