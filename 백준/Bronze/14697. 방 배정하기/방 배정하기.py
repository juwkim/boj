A, B, C, N = map(int, input().split())
flag = 0
for x in range(N//A + 1):
    for y in range((N-x*A)//B + 1):
        z = (N-x*A-y*B)/C
        if z == int(z):
            flag = 1
            break
    if flag:
        break
print(flag) 