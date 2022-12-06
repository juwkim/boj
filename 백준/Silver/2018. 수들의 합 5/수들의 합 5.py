N = int(input())
i, j = 1, 1
num = 0
cnt = 0
while j <= N + 1:
    if num == N:
        cnt += 1
        num += j - i
        i += 1
        j += 1
    elif num > N:
        num -= i
        i += 1
    else:
        num += j
        j += 1
print(cnt)